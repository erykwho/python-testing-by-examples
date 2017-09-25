# Unit Testing with Python 3

## Summary

### Examples
#### Mocking
* [Reading / Writing on Files][reading-writing-on-files]
* [Mocking a method call][mocking-a-method-call]

### Tutorials
#### Mocking
* **[Essentials][essentials]**
    * [Patch][patch]
    * [The Mock Object][the-mock-object]
    * [How to mock][how-to-mock]

* **[Jedi master level of mocking][advanced]**
#### Coverage

Just do this...
```` bash
coverage run --source=. -m unittest discover
coverage report -m
````
----

## DAFUCK IS A TEST?

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

Let's say I have a method called `mama()`. `mama()` does a lot of things. `mama()` calls a weird function called `weirdo()`

```` python
# weirdo() is a method you will want to mock
def weirdo(a_string):
    # Do a bunch of bunch of bunches of things
    # Do more things
    # Opens a fucking file
    # OMG. weirdo() is making 500 HTTP requests
    # weirdo is being weirdo
    return a_string

# mama() is a method you will want to test
def mama():
    i_am_a_variable = "IMA STRING"
    weirdo_response = weirdo(i_am_a_variable)
    return weirdo_response + '1'
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
OMG.. What did happened here?

Did you see this `patch()`? WTF?
Could you understand what he is doing?
Does it make **sense**?
Did you like it?
Did you love it?

No matter if you like it or not, testing is essential.
And tests generally involves mocking methods.

So if you make programs with Python and you don't know how to test your code, i recommend to you to start learning.

**It's necessary.**

## How can I learn testing?

Come here. Come closer.

**[I'll teach you how.][summary]**

![gif-come-here]

My plans with this repository is to to teach ~~you~~ me how to master on python fucking testing.


## Credits
* **date_pattern package:** http://www.onlamp.com/pub/a/python/2005/02/03/tdd_pyunit2.html?page=3
* **mock:** https://docs.python.org/3/library/unittest.mock.html
* **mock.assert_\*:** https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock.assert_called
* **testing with python:** https://donkirkby.github.io/testing/


[specification]: http://langrsoft.com/2006/06/05/are-tests-specs/
[gif-come-here]: https://media.giphy.com/media/3ohA2VpfGovSNE8ESI/giphy.gif

[summary]: ./docs/en/

[be-patient]: https://media.giphy.com/media/xT9KVmZwJl7fnigeAg/giphy.gif

[reading-writing-on-files]: ./docs/en/mocking/examples/reading-writing-on-files.md
[mocking-a-method-call]: ./docs/en/mocking/examples/mocking-a-method-call.md
[essentials]: ./docs/en/mocking/essentials
[advanced]: ./docs/en/mocking/advanced


[patch]: ./docs/en/mocking/essentials/patch.md
[how-to-mock]: ./docs/en/mocking/essentials/how-to-mock.md
[the-mock-object]: ./docs/en/mocking/essentials/the-mock-object.md