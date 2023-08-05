Tips about shlex
================

import the shlex module.::

  >>> import shlex

split
-----

The most common usage::

  >>> cmd = "ls -la /usr"
  >>> shlex.split(cmd)
  ['ls', '-la', '/usr']

How about command with pipe?::

  >>> cmd = "ls -la /usr | cat -n"
  >>> shlex.split(cmd)
  ['ls', '-la', '/usr', '|', 'cat', '-n']
