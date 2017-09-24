import unittest
from unittest.mock import patch

from examples.mocking_a_method_call.get_countries import get_countries


class TestGetCountriesWithPatchAsDecorator(unittest.TestCase):
    @patch('examples.mocking_a_method_call.get_countries.requests.get')
    def test_get_countries(self, mock_http_get):
        expected_countries = ['Brazil', 'The rest of the world']
        fake_url = 'http://ima.fake.url'

        mock_http_get_response = mock_http_get.return_value
        mock_http_get_response.json.return_value = {
            'countries': expected_countries
        }

        actual_countries = get_countries(fake_url)

        mock_http_get.assert_called_once_with(fake_url)

        self.assertEqual(expected_countries, actual_countries)


class TestGetCountriesWithStraightForward(unittest.TestCase):
    def setUp(self):
        patcher = patch('examples.mocking_a_method_call.get_countries.requests.get')
        self.mock_http_get = patcher.start()
        self.addCleanup(patch.stopall)

    def test_get_countries(self):
        expected_countries = ['Brazil', 'The rest of the world']
        fake_url = 'http://ima.fake.url'

        mock_http_get_response = self.mock_http_get.return_value
        mock_http_get_response.json.return_value = {
            'countries': expected_countries
        }

        actual_countries = get_countries(fake_url)

        self.mock_http_get.assert_called_once_with(fake_url)

        self.assertEqual(expected_countries, actual_countries)


class TestGetCountriesWithContextManagerPatch(unittest.TestCase):
    def test_get_countries(self):
        with patch('examples.mocking_a_method_call.get_countries.requests.get') as mock_http_get:
            expected_countries = ['Brazil', 'The rest of the world']
            fake_url = 'http://ima.fake.url'

            mock_http_get_response = mock_http_get.return_value
            mock_http_get_response.json.return_value = {
                'countries': expected_countries
            }

            actual_countries = get_countries(fake_url)

            mock_http_get.assert_called_once_with(fake_url)

        self.assertEqual(expected_countries, actual_countries)
