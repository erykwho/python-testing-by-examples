import unittest
from unittest.mock import patch, mock_open

from examples.write_on_file.file_writer import FileWriter


class TestFileWriter(unittest.TestCase):
    def test_file_writer(self):
        fake_file_path = "fake/file/path"
        content = "Message to write on file to be written"
        with patch('examples.write_on_file.file_writer.open', mock_open()) as mocked_file:
            FileWriter().write(fake_file_path, content)

            # assert if opened file on write mode 'w'
            mocked_file.assert_called_once_with(fake_file_path, 'w')

            # assert if the specific content was written in file
            mocked_file().write.assert_called_once_with(content)
