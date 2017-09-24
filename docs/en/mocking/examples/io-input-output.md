# I/O

Or **Input/Output**

or just **working with files**

## Reading Files

Let's say I have a method that returns the number of lines from a file.


```` python
class FileReader:

    @staticmethod
    def count_lines(file_path):
        with open(file_path, 'r') as _file:
            file_content_list = _file.readlines()
            print(file_content_list)
            return len(file_content_list)

````

But I don't want to open a real file. I wanna **mock the opening** and **the content** of the file.
This is *elegantly possible* with [mock_open][mock_open].

This replace the use of `open()`.

This works with both `open()` called directly like this:
```` python
>> file = open('file/path', r)
````

and with a context manager like this:
```` python
with open('file/path', r) as _file:
    # ...
````

### Using mock_open (see the [docs][official-documentation-mock-open])
We are going to use **patch with *parameter*** `new=mock_open()`, so the target is replaced with a **mock_open**.

`mock_open()` has a parameter called `read_data` that is a string for the `read()`, `readline()` and `readlines()` methods of the file opened.

Here is how to mock the file opening and reading with a context manager.

```` python
with patch('__main__.open', new=mock_open(read_data='Fooooo')) as _file:
    # do your call to path 'foo/bar'
    _file.assert_called_once_with('foo/bar', 'r')
````

#### FAQ about this code

> Whatafuck is a context manager?
> It's basically using the `with ..... as variable:` syntax.
> More details [here][python-context-manager].

> Whatafuck is that **'\_\_main\_\_.open'**?
> That, my friend, is the reference for where the object **open** is being *looked up*. In the example above, that `__main__.open` doesn't make sense by itself because there is no object being called.
> More details in the [official doc][official-documentation-where-to-patch].

> Whatafuck is that **assert_called_once_with**?
> You are asserting that `self` is being called only one time with the given parameters.
> Check it out [here][assert_called].

I ~~bet my ass~~ am pretty sure that you are fucking ready to test our method `count_lines()` now.

So let's check out the test code.

```` python
import unittest
from unittest.mock import patch, mock_open

from examples.count_lines.file_reader import FileReader


class TestReadFiles(unittest.TestCase):
    def test_count_lines(self):
        file_content_mock = """Hello World!!
Hello World is in a file.
A mocked file.
He is not real.
But he think he is.
He doesn't know he is mocked"""
        fake_file_path = 'file/path/mock'

        with patch('examples.count_lines.file_reader.open'.format(__name__),
                   new=mock_open(read_data=file_content_mock)) as _file:
            actual = FileReader().count_lines(fake_file_path)
            _file.assert_called_once_with(fake_file_path, 'r')

        expected = len(file_content_mock.split('\n'))
        self.assertEqual(expected, actual)
````

See the [source code][count-lines-source-code]

## Writing on Files

**In development**

## Credits
* [Official documentation][official-documentation]



[official-documentation]: https://docs.python.org/3/library/unittest.mock.html
[official-documentation-mock-open]: https://docs.python.org/3/library/unittest.mock.html#mock-open
[official-documentation-where-to-patch]: https://docs.python.org/3/library/unittest.mock.html#where-to-patch

[python-context-manager]: https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

[count-lines-source-code]: https://github.com/otrabalhador/python-testing-by-examples/tree/master/examples/count_lines

[mock_open]: https://docs.python.org/3/library/unittest.mock.html#mock-open
[patch]: ../essentials/patch.md
[assert_called]: https://http.cat/204

[wait]: https://media.giphy.com/media/xT9KVmZwJl7fnigeAg/giphy.gif