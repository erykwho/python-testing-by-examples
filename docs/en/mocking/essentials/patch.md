# Patch

In simple words, `patch()` will temporarily change the object referenced with another one (*default: MagicMock object*).

Don't know what a MagicMock or a mock object is?
Come [here][mock-object] for a brief explanation of the mock object.

Patch can be used in three ways:
* Context manager
* Decorator
* Straight-forward

## Example

```` python
def foo():
    pass
````

### Patch as context manager

```` python
from unittest.mock import patch

# __main__.foo is the reference of method foo
with patch('__main__.foo') as foo_mock:
    foo_mock.return_value = 3
    print(foo_mock())
    print(foo())

````

### Patch as decorator of another function

```` python
from unittest.mock import patch

# __main__.foo is the reference of method foo
@patch('__main__.foo')
def fake_mock(foo_mock):
    foo_mock.return_value = 3
    print(foo_mock())
    print(foo())

fake_mock()
````

### Straight-forward patch

```` python
from unittest.mock import patch

# __main__.foo is the reference of method foo
patcher = patch('__main__.foo')
foo_mock = patcher.start()
foo_mock.return_value = 3
print(foo_mock())
print(foo())
patcher.stop()
````

## Parameter *Target*

It's time to understand the **\_\_main\_\_.foo** of `patch('__main__.foo')` from the example above.

This is where the object is looked up. More details in the official doc on [where to patch][]

I believe this is enough for most of your tests.
Wanna know more about patch? Come to the [advanced patch tutorial][advanced-patch]

![Be patient][be-patient]

## Go to
* [examples][examples]
* [advanced mocking][advanced]
* [the essentials of mocking][essentials]
* [mocking main menu][mocking-main-menu]
* [summary][summary]

[official-documentation-where-to-patch]: https://docs.python.org/3/library/unittest.mock.html#id5

[advanced]: ../advanced
[examples]: ../examples
[essentials]: ../essentials
[mocking-main-menu]: ../
[summary]: ../../

[advanced-patch]: ../advanced/patch.md
[mock-object]: ./the-mock-object.md

[be-patient]: https://media.giphy.com/media/xT9KVmZwJl7fnigeAg/giphy.gif
