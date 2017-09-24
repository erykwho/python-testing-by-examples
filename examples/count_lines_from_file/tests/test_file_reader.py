
import unittest
from unittest.mock import patch, mock_open

from examples.count_lines_from_file.file_reader import FileReader


class TestReadFiles(unittest.TestCase):
    def test_count_lines(self):
        file_content_mock = """Hello World!!
Hello World is in a file.
A mocked file.
He is not real.
But he think he is.
He doesn't know he is mocked"""
        fake_file_path = 'file/path/mock'

        with patch('examples.count_lines_from_file.file_reader.open'.format(__name__),
                   new=mock_open(read_data=file_content_mock)) as _file:
            actual = FileReader().count_lines(fake_file_path)
            _file.assert_called_once_with(fake_file_path, 'r')

        expected = len(file_content_mock.split('\n'))
        self.assertEqual(expected, actual)