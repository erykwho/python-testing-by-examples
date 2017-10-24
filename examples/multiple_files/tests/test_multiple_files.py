import os
import tempfile
import unittest

from examples.multiple_files.multiple_files import FileUtils


class TestSplitFileInTwo(unittest.TestCase):
    def setUp(self):
        self.file_path_1 = tempfile.mkstemp()[1]
        self.file_path_2 = tempfile.mkstemp()[1]
        self.file_path_3 = tempfile.mkstemp()[1]

        self.expected_content_file_2 = 'line 1\nline 2\n'
        self.expected_content_file_3 = 'line 3\nline 4\nline 5\n'
        self.content = self.expected_content_file_2 + self.expected_content_file_3

        file_1 = open(self.file_path_1, 'w')
        file_1.write(self.content)
        file_1.close()

    def tearDown(self):
        os.remove(self.file_path_1)
        os.remove(self.file_path_2)
        os.remove(self.file_path_3)

    def test_split_in_two_should_have_expected_content(self):
        """Asserts if returned files has the expected content"""

        actual_file_path_2, actual_file_path_3 = \
            FileUtils(self.file_path_1).split_in_two(2, self.file_path_2, self.file_path_3)

        with open(self.file_path_2, 'r') as file:
            file_2_content = file.read()

        with open(self.file_path_3, 'r') as file:
            file_3_content = file.read()

        self.assertEqual(self.expected_content_file_2, file_2_content)
        self.assertEqual(self.expected_content_file_3, file_3_content)
        self.assertEqual((self.file_path_2, self.file_path_3), (actual_file_path_2, actual_file_path_3))
