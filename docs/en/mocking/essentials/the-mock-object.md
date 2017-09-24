# The Mock Object

### Defining a Mock Object

Take a close look at this code.

Try to predict what will happen.

```` python
from unittest.mock import Mock
mock = Mock()
mock.return_value = 3
mock()
mock.assert_called_once_with()
mock()
mock.assert_called_once_with()
````

**Let's read this code together now:**

* In the line `mock = Mock()`, we are instantiating the mock object.

* In the line `mock.return_value = 3`, we are assigning a return value for this instance of the object.
That means that every time I call `mock()` (the instance of `Mock()`), I'll get a value of `3`.

* Look at `mock.assert_called_once_with()`. Here we are asserting that we called the method with no parameters once.
An **AssertionError** will be raised **if this assertion fails**. This happens on the second time we call `mock.assert_called_once_with()`.

**Now you've just learned to assert mocked method calls**

### Mapping method to be mocked by Mock

In development

![Be patient][be-patient]

### Mapping exceptions

In development

![Be patient][be-patient]

### More on side-effect

In development

![Be patient][be-patient]

## Go to
* [examples][examples]
* [advanced mocking][advanced]
* [the essentials of mocking][essentials]
* [mocking main menu][mocking-main-menu]
* [summary][summary]

[advanced]: ../advanced
[examples]: ../examples
[essentials]: ../essentials
[mocking-main-menu]: ../
[summary]: ../../

[be-patient]: https://media.giphy.com/media/xT9KVmZwJl7fnigeAg/giphy.gif
