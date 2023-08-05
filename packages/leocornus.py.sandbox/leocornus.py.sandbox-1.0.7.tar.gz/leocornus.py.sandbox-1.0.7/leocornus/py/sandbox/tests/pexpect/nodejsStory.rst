Story about pexpect and node.js
===============================

How to use pexpect to handle node.js Projects.
::

  >>> import pexpect
  >>> from pexpect import spawn
  >>> import os
  >>> from os import chdir
  >>> from os import path

Handle nodejs Project
---------------------

The **logfile** in **spawn** class is like the **stdout** for subprocess.
If **logfile** is none (which is default), all output will be stream
**before** variable.

prepare some log files
~~~~~~~~~~~~~~~~~~~~~~

get ready the testing folder for log files.
::

  >>> home_folder = path.expanduser("~")
  >>> test_folder = path.join(home_folder, 'pexpect')
  >>> os.mkdir(test_folder)
  >>> path.exists(test_folder)
  True

create log files for buildlog.
::

  >>> build_log = path.join(test_folder, '.buildlog')
  >>> npm_log_file = path.join(test_folder, '.npmlog')
  >>> output = pexpect.run('touch %s' % build_log)
  >>> output = pexpect.run('touch %s' % npm_log_file)
  >>> path.exists(build_log)
  True
  >>> build_log = open(build_log, 'w+r')
  >>> path.exists(npm_log_file)
  True
  >>> npm_log = open(npm_log_file, 'w+r')

Clone a npm project from github
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

using the leocorns-ci-projects
::

  >>> repo_url = 'https://github.com/leocornus/leocornus-ci-projects.git'

Start the http_server, CTRL-C tells the the http_server is started.
::

  >>> chdir(test_folder)
  >>> clone = pexpect.run('git clone --depth=10 %s' % repo_url)
  >>> phonecat_folder = path.join(test_folder, 
  ...                             'leocornus-ci-projects',
  ...                             'projects', 'phonecat')
  >>> chdir(phonecat_folder)
  >>> # set up git to use https
  >>> https = pexpect.run('git config url."https://".insteadof git://')

load the nodjs http_server

spawn directly not seems work will!
::

  >>> http_server = spawn('npm start', logfile=npm_log, timeout=300)
  >>> index = http_server.expect('CTRL-C')
  >>> # try use the send method.
  >>> #http_server.send('aaa')

Try using the bash -c now.
::

  >>> #http_server = spawn('bash -c "npm start > %s&"' % npm_log_file)
  >>> #http_server.expect(pexpect.EOF)

wait the server started.
::

  >>> #import time
  >>> #time.sleep(180) # this is in seconds,

execute the e2e test cases.
::

  ...>>> protractor = spawn('npm run protractor', 
  ......                    logfile=build_log,
  ......                    timeout=300)
  ...>>> index = protractor.expect(pexpect.EOF)
  ...>>> protractor.close()

  >>> from subprocess import check_output
  >>> #protractor = pexpect.run('npm run protractor')
  >>> protractor = check_output(['npm', 'run', 'protractor'])

show the e2e test result.
::

  >>> print(protractor)
  <BLANKLINE>
  >...

  ... >>> print(build_log.read())
  ... >>> print(protractor.before)

shutdown http_server, force close. sendcontrol('c')
we will need the before and after expect match.
::

  >>> #http_server.close(True)
  >>> r = http_server.sendcontrol('c')
  >>> http_server.close()
  >>> print(npm_log.read())

Try to print the whole npm log file.
::

  >>> log = open(npm_log_file)
  >>> content = log.read()
  >>> print(content)
  <BLANKLINE>
  >...

clean up
--------

Just need remove the test folder.
::

  >>> os.chdir(home_folder)
  >>> output = pexpect.run('rm -rf %s' % test_folder)

.. _pexpect: https://github.com/pexpect/pexpect
