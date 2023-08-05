Basic SQLite3
=============

Play around with SQLite3.
::

  >>> import os
  >>> import sqlite3

Assumption
----------

The only assumption is we have SQLite_ installed in desktop.
Sine Python 2.5, **sqlite3** module is one of the core modules of
Python language.
It makes a lot easier to using SQLite_ in Python application.

Travis CI should have SQLite installed.

Preparing
---------

SQLite_ is self-contained and serverless.
So we just need an empty file to get started the SQLite database.

Create database file for testing.
SQLite_ will create the db file if it is NOT exist.
::

  >>> home_folder = os.path.expanduser('~')
  >>> db_file = os.path.join(home_folder, 'sample.db')

Connect to the db file.
::

  >>> conn = sqlite3.connect(db_file)
  >>> print(conn)
  <sqlite3.Connection object ...>

Create tables
-------------

Try to create 2 tables for testing:
::

  >>> c = conn.cursor()
  >>> c = c.execute('''
  ...   CREATE TABLE person
  ...   (id INTEGER PRIMARY KEY ASC, name varchar(250) NOT NULL)
  ...   ''')
  >>> c = c.execute('''
  ...   CREATE TABLE address
  ...   (id INTEGER PRIMARY KEY ASC, street_name varchar(250), street_number varchar(250),
  ...    post_code varchar(250) NOT NULL, person_id INTEGER NOT NULL,
  ...    FOREIGN KEY(person_id) REFERENCES person(id))
  ...   ''')
  >>> c = c.execute('''
  ...   INSERT INTO person VALUES(1, 'pythoncentral')
  ...   ''')
  >>> c = c.execute('''
  ...   INSERT INTO address VALUES(1, 'python road', '1', '00000', 1)
  ...   ''')
  >>> conn.commit()
  >>> #conn.close()

quick query for testing::

  >>> c = c.execute('SELECT * FROM person')
  >>> print c.fetchall()
  [(1, u'pythoncentral')]

Clean up
--------

we only need remove the sample db file.
This will depends on the Fabric_, assume we have this installed.
::

  >>> from fabric.operations import local
  >>> clean = local('rm -rf %s' % db_file, False)
  [localhost] local: rm -rf ...

.. _SQLite: https://www.sqlite.org/
.. _Fabric: http://fabfile.org
