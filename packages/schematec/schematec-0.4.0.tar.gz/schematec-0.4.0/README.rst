Schematec
=========

.. image:: https://travis-ci.org/mylokin/redisext.svg?branch=master
   :target: https://travis-ci.org/mylokin/redisext

Schematec is a set of tools that makes input data validation easier.
The purpose of this code is attempt to bring simplicity to applications
logics using separation of data validation and actual data processing.

Quickstart
----------

.. code:: python

   import schematec as s

   schema = s.dictionary(
      id=s.integer & s.required,
      name=s.string,
      tags=s.array(s.string),
   )

.. code:: python

   >>> data = {
   ...     'id': '1',
   ...     'name': 'Red Hot Chili Peppers',
   ...     'tags': ['funk', 'rock'],
   ...     'rank': '1',
   ... }
   >>> schema(data)
   {'id': 1, 'name': u'Red Hot Chili Peppers', 'tags': [u'funk', u'rock']}


Concepts
--------

Schematec module is based on three basic concepts:

* Schema
* Validator
* Converter

Schema
^^^^^^

Term "schema" is used to describe complex data struct such as dictionary(hashmap)
or array(list). Schemas has two different types of validation (it is not related to
array schemas):

* Strict - requires all values
* Non-strict - tolerate to missed values

`schematec.exc.SchemaError` is raised in case provided data is incorrect.

Order of schema validations:

#. Unbound Validators
#. Schemas(inner)
#. Converters
#. Bound Validators

Validator
^^^^^^^^^

Term "validator" describes callable objects that perform different types of checks.
There are two types of validators in schematec:

* Bound - type related, for example "max length" validator is bound to sized type.
* Unbound - universal, for example "required" validator.

Raises `schematec.exc.ValidationError`.

Schematec provides following validators:

required
   check if value is provided

length
   check iterable for max length

regex
   check if given value is valid

Converter
^^^^^^^^^

Term "converter" is used to describe cast functions. Schematec supports subset of JSON
data types.

Basic types:

- integer(int)
- string(str)
- boolean(bool)

Containers:

- array(list)
- dictionary(dict)

Raises `schematec.exc.ConvertationError`.

Convertation rules
=================

integer
-------

#. Any int or long value
#. Any suitable string/unicode
#. Boolean value

number
-------

#. Any float or int or long value
#. Any suitable string/unicode
#. Boolean value

string
------

#. Any suitable string/unicode
#. Any int or long value

boolean
-------

#. Boolean value
#. 0 or 1
#. '0' or '1'
#. u'0' or u'1'

dictionary
----------

#. Any mapping value(collections.Mapping)

array
-----

#. Any iterable value(collections.Iterable), but not a mapping

Complex Descriptors
===================

"Schema", "validator" and "converter" are internally referenced as "descriptors". Common task is
creation of complex validation rules for a field(or "complex descriptors"). To do this use bitwise
"and" operator on descriptors:

.. code:: python

   >>> import schematec
   >>> schematec.integer & schematec.required
   <schematec.abc.ComplexDescriptor object at 0x10b05a0d0>

Sugar Schema
============

Schematec supports additional "magic" way to define your schemas. You can use simple dicts and lists
to describe your data. For example:

.. code:: python

   >>> import schematec as s
   >>> schema = {
   ...     'a': [{
   ...         'b': s.integer,
   ...     }]
   ... }
   >>> data = {
   ...     'a': [{'b': 1}, {'b': '1'}, {}]
   ... }
   >>> s.process(schema, data)
   {'a': [{'b': 1}, {'b': 1}, {}]}

Examples
========

Recursive schema
----------------

.. code:: python

   import schematec as s

   schema = s.dictionary(
       id=s.integer & s.required,
       entity=s.dictionary(
           name=s.string & s.required,
           value=s.string,
       )
   )

.. code:: python

   >>> data = {
   ...     'id': 1,
   ...     'entity': {
   ...         'name': 'song',
   ...         'value': 'californication',
   ...     }
   ... }
   >>> schema(data)
   {'id': 1, 'entity': {'name': u'song', 'value': u'californication'}}


Errors handling
---------------

.. code:: python

   import schematec as s

   schema = s.dictionary(
       id=s.integer & s.required,
       entity=s.dictionary(
           name=s.string & s.required,
           value=s.string,
       )
   )

.. code:: python

   >>> data = {
   ...     'id': 1,
   ...     'entity': {
   ...         'value': 'californication',
   ...     }
   ... }
   >>> schema(data)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "schematec/schema.py", line 44, in __call__
       value = schema(value, strict=strict)
     File "schematec/schema.py", line 32, in __call__
       validator(name, data)
     File "schematec/validators.py", line 12, in __call__
       raise exc.ValidationError(name)
   schematec.exc.ValidationError: name
