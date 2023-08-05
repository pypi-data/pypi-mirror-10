Tips for using Popen
====================

How to use the Popen class.

Imports
-------

We need the subpress module::

  >>> from os import chdir
  >>> import subprocess
  >>> from subprocess import STDOUT
  >>> from subprocess import PIPE
  >>> from subprocess import Popen
  >>> from subprocess import check_output
  >>> from subprocess import CalledProcessError
  >>> import signal

Run process in backend
----------------------

2 Main requirement:

- be able to run **npm start** in backend.
- be able to stop it completly after successfully run it in backend.

questions and answers:

- does chdir support with context? NO
- could we use a file as stdout? YES 

solution:

- Popen with creationflags = subpress.CREATE_NEW_PROCESS_GROUP! 
  **DOES NOT WORK**
  As this flag only available for Windows.

get ready a file for stdout.
::

  >>> from tempfile import TemporaryFile
  >>> out = TemporaryFile()

::

  >>> chdir('/usr/opspedia/xampp/rd/angular-trac-client')
  >>> path_npm = '/usr/opspedia/xampp/rd/cfgrepo/sample/nodejs/bin'
  >>> path = '$PATH:%s' % path_npm
  >>> p = Popen(['%s/npm' % path_npm, 'start'], stdout=out)
  >>> print(p)
  <subprocess.Popen object at 0x...>

Verify if the server is running in backend?
::

  >>> output = check_output(['npm', 'run', 'protractor'])
  >>> print(output)

terminate or kill the subpress.

- terminate only kills the pid itself instead of the whole group.
- kill is the same as terminate.
- send_signal does NOT work either.
::

  >>> #p.send_signal(signal.SIGINT)
  >>> p.communicate(signal.SIGINT)
