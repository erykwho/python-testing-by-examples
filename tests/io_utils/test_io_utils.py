import tempfile
import unittest
from unittest.mock import patch, mock_open

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

from io_utils import io_utils


class TestIoUtils(unittest.TestCase):
    def test_get_content_from_file_path(self):
        expected = 'banana'
        file_path = ''
        with patch('io_utils.io_utils.open', mock_open(read_data=expected)) as m:
            actual = io_utils.get_content_from_file_path(file_path)
            m.assert_called_once_with(file_path, 'r')

        self.assertEqual(expected, actual)

    def test_return_file_with_extra_text(self):
        extra = "\nIMA mothefucking motherfucka"
        file_content = "banana"
        expected = file_content + extra
        file_path = 'motherfucking/file/path'
        with patch('io_utils.io_utils.open', mock_open(read_data=file_content)) as file:
            actual = io_utils.return_file_with_extra_text(file_path, extra)
            file.assert_called_once_with(file_path, 'r')

        self.assertEqual(expected, actual)


class TestReadContent(unittest.TestCase):
    def setUp(self):
        self.message = 'Hello world'

    def test_write_from_file_path(self):
        file_path = tempfile.mkstemp()[1]
        expected = self.message
        io_utils.write_from_file_path(file_path, expected)
        actual = io_utils.get_content_from_file_path(file_path)

        self.assertEqual(expected, actual)

    def test_write_from_file(self):
        file = StringIO()
        expected = self.message
        io_utils.write_from_file(file, expected)
        file.seek(0)
        actual = file.read()
        self.assertEqual(expected, actual)

