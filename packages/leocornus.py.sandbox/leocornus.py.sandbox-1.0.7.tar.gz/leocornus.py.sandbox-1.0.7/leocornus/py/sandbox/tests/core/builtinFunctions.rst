Built-in Functions Playground
=============================

::

  >>> #s = raw_input('-->')


reversed
--------

The function **reversed** is introduced since Python version 2.4.
::

  >>> some = [1, 2, 3]
  >>> for i in reversed(some):
  ...    print(i)
  3
  2
  1

range
-----

regular usage, the stop number is not included.
::

  >>> range(9, 4, -1)
  [9, 8, 7, 6, 5]
