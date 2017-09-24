import re

import requests


def get_countries(countries_url='http://api.population.io/1.0/countries'):
    request_response = requests.get(countries_url).json()
    return request_response['countries']


def filter_items(items, pattern):
    return [country for country in items if re.match(pattern, country)]


def filter_countries(pattern="B*"):
    print('Filtering countries with the pattern %s' % pattern)
    countries = get_countries()
    filtered_countries = filter_items(countries, pattern)
    print('Countries: %s' % str(filtered_countries))

if __name__ == '__main__':
    pattern_input = input('Regex pattern to filter countries: ')
    filter_countries(pattern_input)
