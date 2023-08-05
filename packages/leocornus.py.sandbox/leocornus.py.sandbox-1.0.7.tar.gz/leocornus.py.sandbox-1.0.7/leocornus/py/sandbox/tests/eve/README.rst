Get started with Eve
====================

The REST API framework for Python.
It actually depends on Flask_ framework.

Eve application is simple
-------------------------

Get ready a mini setting::

  >>> mini_settings = {
  ...   'DOMAIN' : {'people' : {}}
  ... }

Construct the Eve_ app and run it.
::

  >>> from eve import Eve
  >>> from eve_sqlalchemy import SQL
  >>> app = Eve(auth=None, settings=mini_settings, data=SQL)
  >>> #app.run()

Run Eve_ app on uWSGI

`Eve App on uWSGI`_

.. _Eve App on uWSGI: http://stackoverflow.com/questions/22577162/running-python-eve-rest-api-in-production
.. _Eve: http://python-eve.org
.. _Flask: http://flask.pocoo.org/
