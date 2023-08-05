kwargs_obj
===============================

.. image:: https://badge.fury.io/py/kwargs_obj.png
    :target: http://badge.fury.io/py/kwargs_obj

.. image:: https://pypip.in/d/kwargs_obj/badge.png
        :target: https://pypi.python.org/pypi/kwargs_obj


Class that maps ``.__init__(self, **kwargs)`` to attributes.

Documentation
-------------

This module can be used to automatically set values from ``**kwargs`` to attributes, and also to dissable setting of unset attributes.

Examples
++++++++

Map \*\*kwargs to attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Here you can see, how to map ``**kwargs`` to your attributes:

.. code-block:: python

    class Xex(KwargsObj):
        def __init__(self, **kwargs):
            self.something = None
            self.something_else = None

            self._kwargs_to_attributes(kwargs)

This will allow to pass parameters which sets ``something_else`` and ``something_different``:

.. code-block:: python

    >>> x = Xex(something=True)
    >>> x.something
    True

Setting of unset attributes is dissabled:

.. code-block:: python

    >>> x = Xex(asd=True)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "<stdin>", line 5, in __init__
      File "kwargs_obj/kwargs_obj.py", line 61, in _kwargs_to_attributes
        "Can't set %s parameter - it is not defined here!" % key
    ValueError: Can't set asd parameter - it is not defined here!

Disable setting of unset attributes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
There is also modified `.__setattr__()`` method, which disables to set new attributes. This may be good idea for data containers.

Modified `.__setattr__()` functionality can be triggered by setting the ``._all_set`` attribute:

.. code-block:: python

    class Xex(KwargsObj):
        def __init__(self):
            self.something = None
            self.something_else = None

            self._all_set = True

It will be now impossible to set new attributes, which may be good for preventing typos:

.. code-block:: python

    >>> x = Xex()
    >>> x.asd = True
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "kwargs_obj/kwargs_obj.py", line 50, in __setattr__
        raise ValueError("%s is not defined in this class!" % name)
    ValueError: asd is not defined in this class!

But you can still redefine already defined attributes:

.. code-block:: python

    >>> x.something = True
    >>> 
