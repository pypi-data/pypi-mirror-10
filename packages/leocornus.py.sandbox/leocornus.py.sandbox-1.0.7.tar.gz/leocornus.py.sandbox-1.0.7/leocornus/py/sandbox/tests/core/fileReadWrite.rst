How to read and write file in Python
====================================

The builtin function **open** is for read or write a file in Python

open modes
----------

Write to a file is very simple thing in Python language.
The confusion part is the details open options.
Here are commonly-used modes:

:r:
  open a file for reading only.

:w:
  Open a file for writing, truncating the file is it already exists.

:a:
  Open a file for appending, new writes will append to the
  end of the corrent seek position.

The default mode will be **'r'**

Test truncating
---------------

Here are cases we will test.
::

  >>> file_name = 'testing'
  >>> data1 = 'some testing content'
  >>> data2 = 'There are someting else'

Open a file to writing for multiple times.
::

  >>> log = open(file_name, 'w')
  >>> try:
  ...     log.write(data1)
  ... finally:
  ...     log.close()

Read the file to verify content.
The default open mode is **'r'**.
::

  >>> log = open(file_name)
  >>> content = log.read()
  >>> content == data1
  True
  >>> content == data2
  False
  >>> log.close()

Now we open if for write again with content **data2**
::

  >>> log = open(file_name, 'w')
  >>> try:
  ...     log.write(data2)
  ... finally:
  ...     log.close()

Read the conent again. the same file will have completely
different content.
::

  >>> log = open(file_name)
  >>> content = log.read()
  >>> content == data1
  False
  >>> content == data2
  True
  >>> log.close()

clen up the testing file
------------------------

Using the check_output to remove the sigle testing file.
::

  >>> from subprocess import check_output
  >>> output = check_output(['rm', file_name])
