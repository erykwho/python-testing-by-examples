import unittest
from io import StringIO
from unittest.mock import patch, Mock, MagicMock


class Class:
    def method(self):
        pass


with patch('__main__.Class') as MockClass:
    instance = MockClass.return_value
    instance.method.return_value = 'foo'
    assert Class() is instance
    assert Class().method() == 'foo'
    print(Class().method())


def foo():
    pass


patcher = patch('__main__.foo')
foo_mock_1 = patcher.start()
foo_mock_1.return_value = 'FUUUOOOOO'

print(foo())
patcher.stop()

print(foo())

with patch('__main__.foo') as foo_mock:
    foo_mock.return_value = 3

print(foo_mock())


class Printer:
    def __init__(self):
        print('beginning')

    def print_to_stdout(self, message):
        print(message)


def printer():
    print('beginning')


@patch('sys.stdout', new_callable=StringIO)
def test(mock_stdout):
    # printer()
    a = Printer()
    # print(mock_stdout)
    assert mock_stdout.getvalue() == 'beginning\n'


test()


class Foo:
    def foo(self):
        pass


# config = {'foo.return_value': 'ofooofofo', 'other.side_effect': Exception('Boom!')}
# patcher = patch('{}.Foo'.format(__name__), **config)
# mock_foo = patcher.start()

config = {'foo.return_value': 'ofooofofo', 'other.side_effect': Exception('Boom!')}


@patch.object(Foo, 'foo')
def test_obj(mock_method):
    mock_method.return_value = 4
    Foo.foo(3)
    mock_method.assert_called_with(3)
    print(Foo().foo())


test_obj()


@patch('__main__.Foo')
def test_obj_2(mock_class):
    instance = mock_class.return_value
    instance.foo.return_value = 'ofoofooooo'
    print(Foo().foo())
    # Foo.foo(3)
    # mock_class.foo.assert_called_with(3)


test_obj_2()


class TestCaseExample(unittest.TestCase):
    def setUp(self):
        patcher = patch('package.module.Class')
        self.MockClass = patcher.start()
        self.addCleanup(patch.stopall())

    def test_my_foo(self):
        assert package.module.Class is self.MockClass
        assert 1 == 2


@patch('__main__.ord')
def test_ord(mock_ord):
    mock_ord.return_value = 3
    print(ord('c'))


test_ord()


def __str__(self):
    return 'fooble'


mock = Mock()
mock.__str__ = __str__
mock.return_value = 321

print(str(mock))

mock = MagicMock()
mock.__iter__.return_value = iter([1, 2, 3])

for el in list(mock):
    print(el)

mock.__iter__.return_value = iter(['a', 'b', 'c'])
list(mock)

list(mock)
