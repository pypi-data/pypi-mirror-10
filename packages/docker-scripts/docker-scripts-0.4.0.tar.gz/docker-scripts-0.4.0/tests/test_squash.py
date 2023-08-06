import unittest
import mock
import six

from docker_scripts.squash import Squash
from docker_scripts.errors import SquashError


class TestSkippingFiles(unittest.TestCase):

    def setUp(self):
        self.docker_client = mock.Mock()
        self.log = mock.Mock()
        self.image = "whatever"
        self.squash = Squash(self.log, self.image, self.docker_client)

    def test_should_skip_exact_files(self):
        ret = self.squash._file_should_be_skipped(
            '/opt/webserver/something', ['/opt/eap', '/opt/webserver/something'])
        self.assertTrue(ret)

    def test_should_not_skip_file_not_in_path_to_skip(self):
        ret = self.squash._file_should_be_skipped(
            '/opt/webserver/tmp', ['/opt/eap', '/opt/webserver/something'])
        self.assertFalse(ret)

    def test_should_not_skip_the_file_that_name_is_similar_to_skipped_path(self):
        ret = self.squash._file_should_be_skipped(
            '/opt/webserver/tmp1234', ['/opt/eap', '/opt/webserver/tmp'])
        self.assertFalse(ret)

    def test_should_skip_files_in_subdirectory(self):
        ret = self.squash._file_should_be_skipped(
            '/opt/webserver/tmp/abc', ['/opt/eap', '/opt/webserver/tmp'])
        self.assertTrue(ret)


class TestParseImageName(unittest.TestCase):

    def setUp(self):
        self.docker_client = mock.Mock()
        self.log = mock.Mock()
        self.image = "whatever"
        self.squash = Squash(self.log, self.image, self.docker_client)

    def test_should_parse_name_name_with_proper_tag(self):
        self.assertEqual(self.squash._parse_image_name(
            'jboss/wildfly:abc'), ('jboss/wildfly', 'abc'))
        self.assertEqual(
            self.squash._parse_image_name('jboss:abc'), ('jboss', 'abc'))

    def test_should_parse_name_name_without_tag(self):
        self.assertEqual(self.squash._parse_image_name(
            'jboss/wildfly'), ('jboss/wildfly', 'latest'))
        self.assertEqual(
            self.squash._parse_image_name('jboss'), ('jboss', 'latest'))


class TestPrepareTemporaryDirectory(unittest.TestCase):

    def setUp(self):
        self.docker_client = mock.Mock()
        self.log = mock.Mock()
        self.image = "whatever"
        self.squash = Squash(self.log, self.image, self.docker_client)

    @mock.patch('docker_scripts.squash.tempfile')
    def test_create_tmp_directory_if_not_provided(self, mock_tempfile):
        self.squash._prepare_tmp_directory(None)
        mock_tempfile.mkdtemp.assert_called_with(prefix="docker-squash-")

    @mock.patch('docker_scripts.squash.tempfile')
    @mock.patch('docker_scripts.squash.os.path.exists', return_value=True)
    def test_should_raise_if_directory_already_exists(self, mock_path, mock_tempfile):
        with self.assertRaises(SquashError) as cm:
            self.squash._prepare_tmp_directory('tmp')
        self.assertEquals(
            str(cm.exception), "The 'tmp' directory already exists, please remove it before you proceed")
        mock_path.assert_called_with('tmp')
        self.assertTrue(len(mock_tempfile.mkdtemp.mock_calls) == 0)

    @mock.patch('docker_scripts.squash.os.path.exists', return_value=False)
    @mock.patch('docker_scripts.squash.os.makedirs', return_value=False)
    def test_should_use_provided_tmp_dir(self, mock_makedirs, mock_path):
        self.assertEqual(self.squash._prepare_tmp_directory('tmp'), 'tmp')
        mock_path.assert_called_with('tmp')
        mock_makedirs.assert_called_with('tmp')


class TestPrepareLayersToSquash(unittest.TestCase):

    def setUp(self):
        self.docker_client = mock.Mock()
        self.log = mock.Mock()
        self.image = "whatever"
        self.squash = Squash(self.log, self.image, self.docker_client)

    # The order is from oldest to newest
    def test_should_generate_list_of_layers(self):
        self.assertEquals(self.squash._layers_to_squash(
            ['abc', 'def', 'ghi', 'jkl'], 'def'), (['ghi', 'jkl'], ['abc', 'def']))

    def test_should_not_fail_with_empty_list_of_layers(self):
        self.assertEquals(self.squash._layers_to_squash([], 'def'), ([], []))

    def test_should_return_all_layers_if_from_layer_is_not_found(self):
        self.assertEquals(self.squash._layers_to_squash(
            ['abc', 'def', 'ghi', 'jkl'], 'asdasdasd'), (['abc', 'def', 'ghi', 'jkl'], []))


class TestGenerateImageId(unittest.TestCase):

    def setUp(self):
        self.docker_client = mock.Mock()
        self.log = mock.Mock()
        self.image = "whatever"
        self.squash = Squash(self.log, self.image, self.docker_client)

    def test_should_generate_id(self):
        image_id = self.squash._generate_image_id()
        self.assertEquals(len(image_id), 64)
        self.assertEquals(isinstance(image_id, str), True)

    @mock.patch('docker_scripts.squash.hashlib.sha256')
    def test_should_generate_id_that_is_not_integer_shen_shortened(self, mock_random):
        first_pass = mock.Mock()
        first_pass.hexdigest.return_value = '12683859385754f68e0652f13eb771725feff397144cd60886cb5f9800ed3e22'

        second_pass = mock.Mock()
        second_pass.hexdigest.return_value = '10aaeb89980554f68e0652f13eb771725feff397144cd60886cb5f9800ed3e22'

        mock_random.side_effect = [first_pass, second_pass]
        image_id = self.squash._generate_image_id()
        self.assertEquals(mock_random.call_count, 2)
        self.assertEquals(len(image_id), 64)


class TestGenerateRepositoriesJSON(unittest.TestCase):

    def setUp(self):
        self.docker_client = mock.Mock()
        self.log = mock.Mock()
        self.image = "whatever"
        self.squash = Squash(self.log, self.image, self.docker_client)

    def test_generate_json(self):
        image_id = '12323dferwt4awefq23rasf'
        with mock.patch.object(six.moves.builtins, 'open', mock.mock_open()) as mock_file:
            self.squash._generate_repositories_json(
                'file', image_id, 'name', 'tag')
            mock_file().write.assert_called_once_with(
                '{"name": {"tag": "12323dferwt4awefq23rasf"}}')

    def test_handle_empty_image_id(self):
        with mock.patch.object(six.moves.builtins, 'open', mock.mock_open()) as mock_file:
            with self.assertRaises(SquashError) as cm:
                self.squash._generate_repositories_json(
                    'file', None, 'name', 'tag')

            self.assertEquals(
                str(cm.exception), 'Provided image id cannot be null')
            mock_file().write.assert_not_called()


class TestMarkerFiles(unittest.TestCase):

    def setUp(self):
        self.docker_client = mock.Mock()
        self.log = mock.Mock()
        self.image = "whatever"
        self.squash = Squash(self.log, self.image, self.docker_client)

    def _tar_member(self, ret_val):
        member = mock.Mock()
        member.name = ret_val
        return member

    def test_should_find_all_marker_files(self):
        files = []

        for path in ['/opt/eap', '/opt/eap/one', '/opt/eap/.wh.to_skip']:
            files.append(self._tar_member(path))

        tar = mock.Mock()
        tar.getmembers.return_value = files
        markers = self.squash._marker_files(tar)

        self.assertTrue(len(markers) == 1)
        self.assertTrue(list(markers)[0].name == '/opt/eap/.wh.to_skip')

    def test_should_return_empty_dict_when_no_files_are_in_the_tar(self):
        tar = mock.Mock()
        tar.getmembers.return_value = []
        markers = self.squash._marker_files(tar)
        self.assertTrue(markers == {})

    def test_should_return_empty_dict_when_no_marker_files_are_found(self):
        files = []

        for path in ['/opt/eap', '/opt/eap/one']:
            files.append(self._tar_member(path))

        tar = mock.Mock()
        tar.getmembers.return_value = files
        markers = self.squash._marker_files(tar)

        self.assertTrue(len(markers) == 0)
        self.assertTrue(markers == {})

if __name__ == '__main__':
    unittest.main()
