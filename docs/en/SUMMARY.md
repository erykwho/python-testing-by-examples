# Summary

# List of contents
* [Mocking][mocking]


## WHADAFUCK IS A TEST?

If you don't fucking know what is a test, let me tell ya.

> A test is a [specification] for program.

cool..

## What about Unit Testing

The same as for the test, dãã. But for a program unity. For a method, if you wish.

> My method

```` python
def who(ze_bula):
    return "My {}".format(ze_bula)

````

> Can be tested with


```` python
import unittest

class TestWho(unittest.TestCase):
    def test_who(self):
        expected = "My BotoFe"
        actual = who("BotoFe")
        self.assertEqual(expected, actual)

````

Does the code makes fucking sense?
No fucking way!!

But I guarantee to you that is tested.

## Mocks?

Yeah!!

It's awesome aswell.

You don't need to call private functions that does horrifyingly horrifying things that you don't care.
You can mock them.

Let's say I have a method called mama(). `mama()` does a lot of things. `mama()` calls a weird function called `weirdo()`

```` python
# weirdo() is a method you will want to mock
def weirdo(a_string):
    # Do a bunch of bunch of bunches of things
    # Do more things
    # Opens a fucking file
    # OMG. weirdo() is making 500 requests
    # weirdo is being weirdo
    return a_string

# mama() is a method you will want to test
def mama():
    # Look at this comment line and imagine a lot of things
    i_am_a_variable = "IMA STRING"
    omg = weirdo(i_am_a_variable)
    return omg + '1'
````

And let's say, for the sake of this tutorial that probably only I will read, that you are testing `mama()` and you want to fake a return of `weirdo()`.

Is it possible?

Yeah, it is. Look at this:

```` python

import unittest
from unittest.mock import patch

class TestMama(unittest.TestCase):

    @patch('{}.weirdo'.format(__name__))
    def test_mama(self, mock_weirdo):
        mock_weirdo.return_value = "IMA weirdo"

        expected = "IMA weirdo1"
        actual = mama()

        self.assertEqual(expected, actual)

````
OMG, this mock is fucking weird, right?

**Yes and no.**
* Yes if you don't fucking know how to test with python.
* Yes if you disagree with me on how to mock `weirdo()`
* No if you love me.


## How can I learn testing?

Come here. Come closer. I'll teach you how.

![gif-come-here]

My plans with this repository is to to teach ~~you~~ me how to master on python fucking testing.


## Credits
* date_pattern package: http://www.onlamp.com/pub/a/python/2005/02/03/tdd_pyunit2.html?page=3
* mock: https://docs.python.org/3/library/unittest.mock.html
* testing with python: https://donkirkby.github.io/testing/


[specification]: http://langrsoft.com/2006/06/05/are-tests-specs/
[gif-come-here]: https://media.giphy.com/media/3ohA2VpfGovSNE8ESI/giphy.gif
[mocking]: ./mocking
