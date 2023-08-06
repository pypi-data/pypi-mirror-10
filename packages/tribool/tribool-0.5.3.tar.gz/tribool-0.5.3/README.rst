Tribool: Three-Valued Logic
===========================

`Tribool <http://www.grantjenks.com/docs/tribool/>`_ is an Apache2 licensed
Python module that implements three-valued logic.

Suppose for a moment that you're attempting to store a value across a network
connection. You begin with a simple protocol in which the server stores the
received value and then sends an acknowledgement to the client.  In this
design, the client experiences a delay between when the request is sent and the
acknowledgement is received. In that delay, it is impossible for the client to
know whether the value has been committed on the server.  In such cases, it's
useful to describe the commit state of the server from the client's perspective
as True, False, or Indeterminate.

Another example occurs in database systems. Consider a record that contains
a boolean field. Such a field may only be either True or False. But we want
to support the notion of committing a partial record in the case that the
record is large or the client does not have all relevant information. In this
scenario, we wish to commit neither True nor False as the value is currently
Unknown.

The Python Tribool module was designed for these cases by describing a logical
data type that supports three values: True, False, and Indeterminate. The third
value is best thought of as a state being either True or False. Given these
three values it's possible to define truth tables over the logical operators
`and`, `or` and `not` and to define equality and inequality relationships.

Features
--------

- Pure-Python (easy to hack with)
- Fully Documented
- 100% Test Coverage
- Pragmatic Design (mostly a few truth tables and thread-safe singleton pattern)
- Developed on Python 2.7
- Tested on CPython 2.6, 2.7, 3.2, 3.3, 3.4 and PyPy 2.5+, PyPy3 2.4+

Reference and Indices
---------------------

.. toctree::

   api

* `Tribool Documentation`_
* `Tribool at PyPI`_
* `Tribool at GitHub`_
* `Tribool Issue Tracker`_

.. _`Tribool Documentation`: http://www.grantjenks.com/docs/tribool/
.. _`Tribool at PyPI`: https://pypi.python.org/pypi/tribool/
.. _`Tribool at GitHub`: https://github.com/grantjenks/python_tribool/
.. _`Tribool Issue Tracker`: https://github.com/grantjenks/python_tribool/issues/

License
-------

Copyright 2015 Grant Jenks

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
