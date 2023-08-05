Fabric Git Story
================

Using fabric to manipulate git respository.

Our Goal
--------

Brieflly, we will be able to use Fabric to do the following:

- watch a git repository working folder.
- detect the most recent commit.
- keep a build log for each commit.
- checkout the next commit compare to build log.
- execute test (npm test) for the next commit.
- update build log.

We will use a NPM package on github.com as an example.

Setup
-----

imports::

  >>> import os
  >>> from fabric.operations import local
  >>> from fabric.context_managers import lcd

We will use home folder to test this story.
The **prj_folder** will be the working folder for git repo.
::

  >>> home_folder = os.path.expanduser('~')
  >>> test_folder = os.path.join(home_folder, 'test-git')
  >>> os.mkdir(test_folder)
  >>> repo_url = 'https://github.com/leocornus/angular-trac-client.git'
  >>> with lcd(test_folder):
  ...     clone = local('git clone %s' % repo_url, True)
  [localhost] local: git clone ...
  >>> prj0_folder = os.path.join(test_folder, 'angular-trac-client')
  >>> prj_folder = os.path.join(prj0_folder, 'app')

Explore git logs
----------------

Try to find the list of commit id only.
The format option **--format=%h** will make the trick.
::

  >>> with lcd(prj_folder):
  ...     local('git pull', True)
  ...     ids = local('git log --format=%h -10 .', True)
  [localhost] local: git pull
  'Already up-to-date.'
  [localhost] local: git log ...
  >>> ids = ids.splitlines()
  >>> len(ids)
  10

Execute tests
-------------

Try to execute tests commit by commit.
::

  ...>>> with lcd(prj_folder):
  ...     checkout = local('git checkout %s' % ids[1], False)
  ...     config = local('git config url."https://".insteadof git://')
  ...     test = local('npm test', False)
  ...     test = local('npm test', False)
  [localhost] local: git checkout ...
  [localhost] local: git config ...
  [localhost] local: npm test

.cicfg case
-----------

Try to testing the ability to using **.cicfg** file to customize
testing scripts.
This file should have the configuration file format. 
Here is an example file:
::

  >>> from leocornus.py.sandbox.utils_basic import create_file
  >>> ci_scripts = """
  ... [ci]
  ... install:
  ...   npm install
  ... 
  ... script:
  ...   npm test
  ... """
  >>> filename = create_file(prj0_folder, '.cicfg', ci_scripts)

We will using the config parser to read the file and get all scripts.
::

  >>> try:
  ...     import ConfigParser as configparser
  ... except ImportError:
  ...     import configparser
  >>> config = configparser.ConfigParser()
  >>> filename = config.read(filename)
  >>> install = config.get('ci', 'install')
  >>> script = config.get('ci', 'script')
  >>> install = install.strip().splitlines()
  >>> print(install)
  ['npm install']
  >>> script = script.strip().splitlines()
  >>> print(script)
  ['npm test']

no let execute those script.
::

  >>> with lcd(prj0_folder):
  ...     r = local('git config url."https://".insteadof git://')
  ...     r = local('%s >> .log' % install[0], False)
  ...     r = local('%s >> .log' % script[0], False)
  ...     r = local('npm run protractor >> .log',  False)
  ...     r = local('cat .log', False)
  [localhost] local: git config url."https://".insteadof git://
  [localhost] local: npm install >> .log
  [localhost] local: npm test >> .log
  [localhost] local: cat .log

Logic for build log
-------------------

get ready a buildlog.
::

  >>> with lcd(prj_folder):
  ...     log = local('echo %s >> .buildlog' % ids[5], False)
  ...     log = local('echo %s >> .buildlog' % ids[4], False)
  ...     log = local('echo %s >> .buildlog' % ids[3], False)
  ...     log = local('echo %s >> .buildlog' % ids[2], False)
  [localhost] local: echo ... .buildlog
  [localhost] local: echo ... .buildlog
  [localhost] local: echo ... .buildlog
  [localhost] local: echo ... .buildlog

here is the built ids.
::

  >>> with lcd(prj_folder):
  ...     build_ids = local('cat .buildlog', True)
  [localhost] local: cat .buildlog
  >>> build_ids = build_ids.splitlines()
  >>> build_ids[0] == ids[5]
  True
  >>> last_id = build_ids[len(build_ids) - 1]
  >>> last_id == ids[2]
  True

get the one more commit after the latest build id.
The **% ** will be used to escape itself in a format string.
::

  >>> format = '--format=%h'
  >>> with lcd(prj_folder):
  ...     new_ids = local('git log %s %s..' % (format, last_id), True)
  [localhost] local: git log ... 
  >>> new_ids = new_ids.splitlines()
  >>> new_id = new_ids[len(new_ids) - 1]
  >>> new_id == ids[1]
  True

Try to get some details for the new commit: git remote and projcet 
subfolder.
::

  >>> log_option = '--name-only --format=%h -1'
  >>> with lcd(prj_folder):
  ...     remote = local('git remote -v', True)
  ...     branch = local('git branch', True)
  ...     changeset = local('git log %s %s' % (log_option, new_id),
  ...                       True)
  [localhost] local: git remote -v
  [localhost] local: git branch 
  [localhost] local: git log ...
  >>> remote = remote.splitlines()[0]
  >>> remote = remote.strip().split()[1]
  >>> remote == repo_url
  True
  >>> branch = branch.split()[1]
  >>> print(branch)
  master
  >>> change_file = changeset.strip().splitlines()[2]
  >>> folders = change_file.split(os.sep)
  >>> subfolder = os.path.join(folders[0], folders[1])
  >>> print(subfolder)
  app/...

The case that there is no new commit.
::

  >>> last_id = ids[0]
  >>> with lcd(prj_folder):
  ...     new_ids = local('git log %s %s.. .' % (format, last_id), True)
  [localhost] local: git log ...
  >>> new_ids == ""
  True
  >>> not new_ids
  True

Analyze the log message with the following commands::

  $ git log --format=%h --name-only -1 8564fb4
  $ git log --color -1 --name-status 8564fb4

Git sparse checkout
-------------------

The sparse checkout is allow user to checkout one or more subdiectory
ONLY.
We will test the docs folder of angular-trac-client project.
get ready the folder::

  >>> docs_folder = os.path.join(home_folder, 'docs')
  >>> os.mkdir(docs_folder)

Here are the steps::

  >>> name = 'origin'
  >>> with lcd(docs_folder):
  ...     r = local('git init', True)
  ...     r = local('git remote add -f %s %s' % (name, repo_url), True)
  ...     r = local('git config core.sparsecheckout true', True)
  ...     r = local('echo docs/ >> .git/info/sparse-checkout', True)
  ...     r = local('git pull origin master', True)
  ...     r = local('ls -la %s/docs' % docs_folder, True)
  [localhost] local: git init
  [localhost] local: git remote add -f origin ...
  [localhost] local: git config core.sparsecheckout true
  [localhost] local: echo docs/ >> .git/info/sparse-checkout
  [localhost] local: git pull origin master
  [localhost] local: ls -la /home...

Once we pull the latest version, we could checkout a certain 
commit by using the regular checkout command.

Clean up
--------

remove the projec folder to clean up.
::

  >>> rm = local('rm -rf %s' % test_folder, False)
  [localhost] local: rm -rf ...

Remove the sparse checkout folder.
::

  >>> rm = local('rm -rf %s' % docs_folder, False)
  [localhost] local: rm -rf ...
