# Code
def foo_what(a_str):
    b_str = "WHAT?"
    return a_str + b_str


def bar(a_str):
    final_str = foo_what(a_str)
    return final_str

# Test
import unittest
from unittest.mock import patch


class TestBar(unittest.TestCase):
    @patch('foo.foo_what')
    def test_bar(self, mock_foo_what):
        text = 'strWAT'
        mock_foo_what.return_value = 'strWAT'

        bar('str')

        mock_foo_what.assert_called_once_with('str')
        self.assertEqual(text, bar('str'))
