Aglyph is a Dependency Injection framework for Python 2.7+, supporting
type 2 (setter) and type 3 (constructor) injection.

Aglyph runs on CPython (http://www.python.org/) 2.7 and 3.1 - 3.4, and on
recent versions of the PyPy (http://pypy.org/>),
Jython (http://www.jython.org/), IronPython (http://ironpython.net/),
and Stackless Python (http://www.stackless.com/) variants.

Aglyph can assemble "prototype" components (a new instance is created
every time), "singleton" components (the same instance is returned every
time), "borg" components (a new instance is created every time, but all
instances of the same class share the same internal state), and "weakref"
components (the same instance is returned as long as there is at least one
"live" reference to the instance in the running application).

Aglyph can be configured using a declarative XML syntax, or
programmatically in pure Python.


