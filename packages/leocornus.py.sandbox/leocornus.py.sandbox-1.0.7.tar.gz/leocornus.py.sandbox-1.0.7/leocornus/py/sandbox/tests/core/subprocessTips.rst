Tips for subprocess
===================

import modules and utilities::

  >>> from subprocess import STDOUT
  >>> from subprocess import PIPE
  >>> from subprocess import Popen
  >>> from subprocess import check_output
  >>> from subprocess import check_call
  >>> from subprocess import CalledProcessError

check_output and exit status
----------------------------

Each shell command has an exit status (return code).
If the exit status is 0, 
it means the command is executed successfully.
A non-zero exit status normally tells the failure execution.

Test a command which is running successfully::

  >>> output = check_output(["ls", "-la", "/usr"])
  >>> print(output)
  total ...

If It is failed to execute, the CalledProcessError will be expected.
We need set the **stderr** to be **subprocess.STDOUT**.
::

  >>> output = ""
  >>> returncode = 0
  >>> try:
  ...   output = check_output(["ls", "-la", "NONE_EXIT"], 
  ...                         stderr=STDOUT)
  ... except CalledProcessError as cpe:
  ...   output = cpe.output
  ...   returncode = cpe.returncode
  >>> print(output)
  ls: ...
  >>> returncode > 0
  True
  >>> print(returncode)
  2

check_output and >>
-------------------

we cannot use >> in check_output.
::

  >>> file_name = 'log'
  >>> try:
  ...   output = check_output(["ls", "-la", ">>", file_name], 
  ...                         stderr=STDOUT)
  ...   returncode = 0
  ... except CalledProcessError as cpe:
  ...   output = cpe.output
  ...   returncode = cpe.returncode
  >>> print(output)
  ls: ... No such file or directory
  ls: ... No such file or directory
  >>> print(returncode)
  2

We could use the **stdout** parameter of check_output
::

  >>> log = open('log', 'w')
  >>> try:
  ...   returncode = check_call(["ls", "-la"], stdout=log,
  ...                           stderr=STDOUT)
  ... except CalledProcessError as cpe:
  ...   returncode = cpe.returncode
  >>> print(returncode)
  0
  >>> log = open('log', 'r')
  >>> print(log.read())
  total ...

Test error return code, by find some no exist file.
::

  >>> log = open('log', 'w')
  >>> try:
  ...   returncode = check_call(["ls", "-la", 'noexist'], stdout=log,
  ...                           stderr=STDOUT)
  ... except CalledProcessError as cpe:
  ...   returncode = cpe.returncode
  >>> print(returncode)
  2 
  >>> log = open('log', 'r')
  >>> print(log.read())
  ls: ... No such file or directory

remove the testing log file.
::

  >>> rm = check_output(['rm', 'log'])
  >>> print(rm)

check_output and pipe
---------------------

It is very easy to hadle pipe by uing subprocess module.

The following example will add line number to the output of ls,
by using the **cat -n** option.
It is the same with command: **ls -la /usr | cat -n**.
::

  >>> ls = Popen(['ls', '-la', '/usr'], stdout=PIPE)
  >>> output = check_output(['cat', '-n'], stdin=ls.stdout)
  >>> print(output)
   1...total...

We could add more than one pipe.
The following example will simulate command:
**ls -la /usr | cat -n | wc -l**.
We have to close the pipe properly right after it is been used.
::

  >>> ls = Popen(['ls', '-la', '/usr'], stdout=PIPE)
  >>> catls = Popen(['cat', '-n'], stdout=PIPE, stdin=ls.stdout)
  >>> #ls.stdout.close()
  >>> output = check_output(['wc', '-l'], stdin=catls.stdout)
  >>> #catls.stdout.close()
  >>> output > 1
  True

Popen tips
----------

**Popen** class will execute a child program in a new process.
The variable **pid** will return the porcess id.
::

  >>> ls = Popen(['ls'], shell=True)
  >>> ls.pid > 0
  True
