# Mocking a method call

Imagine a method that makes an **HTTP request**. Let's call him **MethodX**.

**MethodX** is being called from another method. Guess what.. this another method will be called **MethodY**.

If we are testing **MethodY**, can we mock **MethodX** so our **test doesn't make the HTTP request**?

![Of Course][of-course-gif]

In this example we are going to mock a **GET HTTP request** that fetches a list of countries from a [world population API][population-api].

Also, we will assert if our method is calling the right url `http://api.population.io/1.0/countries`.

With that in mind, we ~~disobey [TDD][wikipedia-TDD]~~ write our method to be tested before the test itself:

```` python
def get_countries():
    countries_url = 'http://api.population.io/1.0/countries'
    request_response = requests.get(countries_url).json()
    return request_response['countries']
````

Look at this filthy piece of code: `requests.get(countries_url).json()`.

This is where the HTTP request will be made.

## How can we mock it?

### Using patch

#### Using patch as decorator
You will use the `@patch('package.module.method')` decorator just before the test method.
This will create the mock that will be passed as parameter to your test function.

```` python
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
````
#### Using a straight-forward patch
```` python

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
````
#### Using patch as context manager
```` python
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
````

See the [source code][mocking-a-method-call-source-code]

### So many ways to mock...

Yeah, there is.

Actually, all of this [wibbly wobbly timey wimey][wibbly-wobbly-timey-wimey] stuff is centered on the **unittest Mock object**.

Further details [here][how-to-mock].

Also, see the [official docs][official-documentation-mock-object]

## What about now?
* See other [examples][examples]
* Go to [advanced mocking][advanced]
* Go to [the essentials of mocking][essentials]
* Go to [mocking main menu][mocking-main-menu]
* Go to [summary][summary]


[official-documentation-mock-object]: https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
[official-documentation-nesting-patch-decorators]: https://docs.python.org/3/library/unittest.mock.html#nesting-patch-decorators

[wikipedia-TDD]: https://pt.wikipedia.org/wiki/Test_Driven_Development

[population-api]: http://api.population.io/

[advanced]: ../advanced
[examples]: ../examples
[essentials]: ../essentials
[mocking-main-menu]: ../
[summary]: ../../

[how-to-mock]: ../essentials/how-to-mock.md
[the-mock-object]: ../essentials/the-mock-object.md

[mocking-a-method-call-source-code]: https://github.com/otrabalhador/python-testing-by-examples/tree/master/examples/mocking_a_method_call

[wait-gif]: https://media.giphy.com/media/xT9KVmZwJl7fnigeAg/giphy.gif
[of-course-gif]: https://media.giphy.com/media/l41YfdYdptDB9RHIA/giphy.gif
[wibbly-wobbly-timey-wimey]: https://www.youtube.com/watch?v=q2nNzNo_Xps
