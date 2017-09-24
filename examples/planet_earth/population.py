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

