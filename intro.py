import unittest
from unittest.mock import patch


def who(ze_bula):
    return "My {}".format(ze_bula)


class TestWho(unittest.TestCase):
    def test_who(self):
        expected = "My BotoFe"
        actual = who("BotoFe")
        self.assertEqual(expected, actual)


def mama():
    # Look at this comment line and imagine a lot of things
    i_am_a_variable = "IMA STRING"
    omg = weirdo(i_am_a_variable)
    return omg + '1'


def weirdo(a_string):
    # Do a bunch of bunch of bunches of things
    # Do more things
    # Opens a fucking file
    # OMG. weirdo() is making 500 requests
    # weirdo is being weirdo
    return a_string


class TestMama(unittest.TestCase):
    @patch('{}.weirdo'.format(__name__))
    def test_mama(self, mock_weirdo):
        mock_weirdo.return_value = "IMA weirdo"

        expected = "IMA weirdo1"
        actual = mama()

        self.assertEqual(expected, actual)
