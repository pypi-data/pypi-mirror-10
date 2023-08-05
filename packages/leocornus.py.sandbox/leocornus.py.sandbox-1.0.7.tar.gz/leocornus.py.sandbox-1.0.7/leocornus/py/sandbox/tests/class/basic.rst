Python Class in Basic
=====================

Python language is the best OOP language ever!

Define a class
--------------

Define a class is very simple in Python::

  >>> class People(object):
  ...     """People class"""
  ...     # class variable, general things.
  ...     general = []
  ...
  ...     # instance variables
  ...     def __init__(self, name, gender):
  ...         self.name = name
  ...         self.gender = gender

How to use a class?

Here is the class doc::

  >>> print(People.__doc__)
  People class

Here are how to create an instance of a class::

  >>> one = People("One", "Male")
  >>> two = People("Two", "Female")
  >>> print(one.name)
  One
  >>> print(two.gender)
  Female

Inherite a class
----------------

explore the inheritance of a Python class::

  >>> class Man(People):
  ...     """Man class"""
  ...
  ...     def __init__(self, name):
  ...         #self.name = name
  ...         #self.gender = "Male"
  ...         # using the super() function to call parent class's 
  ...         # method.
  ...         super(Man, self).__init__("name", "Male")

testing the child class::

  >>> one = Man("one")
  >>> print(one.gender)
  Male

TypeError: must be type, not classobj
-------------------------------------

This error will be throw out if yuou define a class link following::

  class People():
      """People Class"""

The correct way is like following::

  class People(object):
      """People class"""

