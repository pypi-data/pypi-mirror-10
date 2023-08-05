Overview
========

This is for testing the basic usage for Fabric's local operator.
The local operator is used to run commands on local machine.
::

  >>> from fabric.operations import local
  >>> from fabric.context_managers import lcd
  >>> import os

Very basic things.
The with context was introduced since Python 2.7
::

  >>> with lcd('/usr'):
  ...     local('pwd', True)
  ...     local('ls -la', False)
  ...     local('pwd', False)
  [localhost] local: pwd
  '/usr'
  [localhost] local: ls -la
  ''
  [localhost] local: pwd
  ''

Local operations
----------------

how fabric handle output of the local operations?
The param capture will tell where the output go.
If it is **True**, all output will be packaged as return value.
If it is **False**, all output will be print out on console.
::

  >>> homeFolder = os.path.expanduser('~')
  >>> ret = local('pwd', True)
  [localhost] local: pwd
  >>> print(ret) # doctest 
  /...

Mini CI
-------

We will try to implement a mini CI here.
Try to simulate the following task:

- clone a git repository, for example from github.com
- execute the test case
- analytze the test result. be able to know the test are
  success or failed.
::

  >>> with lcd(homeFolder):
  ...     clone = local('git clone https://github.com/leocornus/leocornus.recipe.distribute.git', False)
  [localhost] local: git clone ...
  >>> testFolder = os.path.join(homeFolder, 'leocornus.recipe.distribute')
  >>> with lcd(testFolder):
  ...     boot = local('python bootstrap.py', False)
  ...     build = local('bin/buildout', False)
  ...     test = local('bin/test -vvcp', False)
  [localhost] local: python bootstrap.py
  [localhost] local: bin/buildout
  [localhost] local: bin/test -vvcp

**clean up**

need remove the whole folder and get ready for next one...
::

  >>> remove = local('rm -rf %s' % testFolder, False)
  [localhost] local: rm -rf ...

Testing copy files.
