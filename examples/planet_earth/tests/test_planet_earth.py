import unittest
from unittest.mock import patch

from examples.planet_earth.population import Population


class TestPlanetEarth(unittest.TestCase):
    @patch('requests.get')
    def test_get_countries(self, mock_get):
        expected = ['Brazil', 'The rest']
        mock_get.return_value.json.return_value = {
            'countries': expected
        }

        planet_earth = Population()
        actual = planet_earth.countries()

        mock_get.assert_called_once_with(planet_earth.countries_url)
        self.assertEqual(expected, actual)

    @patch('requests.get')
    def test_get_countries_with_pattern(self, mock_get):
        countries = ['Brazil', 'The rest', 'Some other country', 'Balululap']
        mock_get.return_value.json.return_value = {'countries': countries}
        expected = ['Brazil', 'Balululap']

        planet_earth = Population()
        actual = planet_earth.countries_with_pattern('(Ba)|(Br)')

        mock_get.assert_called_once_with(planet_earth.countries_url)

        self.assertEqual(expected, actual)
