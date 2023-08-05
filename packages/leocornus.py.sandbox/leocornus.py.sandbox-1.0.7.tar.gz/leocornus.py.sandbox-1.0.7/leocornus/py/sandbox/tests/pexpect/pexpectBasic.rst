Basic (core) Pexpect
====================

Explore the core components of pexpect_.
::

  >>> import pexpect
  >>> import os
  >>> from os import chdir
  >>> from os import path

.. contents:: Table of Contents
   :depth: 5

Basic run
---------

What's the output for the **run** method?
::

  >>> output = pexpect.run('ls -la')
  >>> print(output)
  total ...

Basic spawn
-----------

The class **spawn** is the main class for pexpect_.
::

  >>> from pexpect import spawn

run the command **ls -la** by using the spawn class.
::

  >>> http_server = spawn('ls -la')
  >>> print(http_server.before)
  None
  >>> # expect returns the index of the pattern in the list.
  >>> index = http_server.expect(pexpect.EOF)
  >>> print(http_server.before)
  total ... 
  >>> http_server.close()
  >>> # exist status is 0 tells the command execute successfully.
  >>> print(http_server.exitstatus)
  0

testing the return code:

:0:
  executed successfully

:none-zero:
  failed for error

::

  >>> none_exist =spawn('ls -la NONE_exist')
  >>> index = none_exist.expect(pexpect.EOF)
  >>> print(none_exist.before)
  /...NONE_exist: No such file or directory
  >>> none_exist.close()
  >>> none_exist.exitstatus > 0
  True

spawn bash
----------

Try to manipulate a bash terminal.
::

  >>> shell = spawn('bash', maxread=1)
  >>> shell.isalive()
  True
  >>> i = shell.expect('\$ ')
  >>> c = shell.sendline('pwd')
  >>> i = shell.expect('\$ ')
  >>> c = shell.sendline('exit')
  >>> i = shell.expect(pexpect.EOF)
  >>> shell.isalive()
  False
  >>> shell.close()
