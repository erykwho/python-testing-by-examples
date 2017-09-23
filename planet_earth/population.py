import requests
import re


class Population:
    def __init__(self):
        self.population_api_url = 'http://api.population.io/1.0/'
        self.countries_url = 'http://api.population.io/1.0/countries'

    def countries(self):
        request_response = requests.get(self.countries_url).json()
        return request_response['countries']

    def countries_with_pattern(self, pattern):
        return [country for country in self.countries() if re.match(pattern, country)]


import unittest
from unittest.mock import patch


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


