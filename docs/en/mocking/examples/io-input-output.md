# I/O

Or **Input/Output**

or just **working with files**

* [Reading Files][reading-files]
* [Writing on Files][writing-on-files]

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

### Using mock_open
**see the [docs][official-documentation-mock-open]**

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

Let's make the simplest. A method that **receives a message** and **write it on a file** given a specific **file_path**.

```` python
class FileWriter:
    @staticmethod
    def write(file_path, content):
        with open(file_path, 'w') as file:
            file.write(content)
````

To mock the opening file and writing content on it, we can use `mock_open()`[official-documentation-mock-open].
The mock for this object will be similar to what we've previously seen in [Reading Files][reading-files], with the exception that we don't need to pass the parameter `read_data` in `mock_open()`, because we are not retrieving data from the file.

### How the assertion will look like?
To answer this question, we need to ask ourselves:
> What do we want to test in this function?

A nice test case, in my delusional opinion, will test if a **specific file_path** was called on `open()`, with a specific **open mode**, and if a **specific content** was **written** in the file.

The [**Mock**][official-documentation-mock-object] object implements assertions that could help us testing that.
The one that will be useful to us is `MockObject.assert_called_once_with()`.

Let's take a look on the test?

```` python
import unittest
from unittest.mock import patch, mock_open

from examples.write_on_file.file_writer import FileWriter


class TestFileWriter(unittest.TestCase):
    def test_file_writer(self):
        fake_file_path = "fake/file/path"
        content = "Message to write on file to be written"
        with patch('examples.write_on_file.file_writer.open', mock_open()) as mocked_file:
            FileWriter().write(fake_file_path, content)

            # assert if opened file on write mode 'w'
            mocked_file.assert_called_once_with(fake_file_path, 'w')

            # assert if write(content) was called from the file opened
            # in another words, assert if the specific content was written in file
            mocked_file().write.assert_called_once_with(content)

````

See the [source code][write-on-file-source-code].

## Credits
* [Official documentation][official-documentation]



[official-documentation]: https://docs.python.org/3/library/unittest.mock.html
[official-documentation-mock-open]: https://docs.python.org/3/library/unittest.mock.html#mock-open
[official-documentation-where-to-patch]: https://docs.python.org/3/library/unittest.mock.html#where-to-patch
[official-documentation-mock-object]: https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock

[python-context-manager]: https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

[count-lines-source-code]: https://github.com/otrabalhador/python-testing-by-examples/tree/master/examples/count_lines
[write-on-file-source-code]: https://github.com/otrabalhador/python-testing-by-examples/tree/master/examples/write_on_file

[mock_open]: https://docs.python.org/3/library/unittest.mock.html#mock-open
[patch]: ../essentials/patch.md
[assert_called]: https://http.cat/204

[wait]: https://media.giphy.com/media/xT9KVmZwJl7fnigeAg/giphy.gif

[reading-files]: ./io-input-output.html#reading-files
[writing-on-files]: ./io-input-output.html#writing-on-files
