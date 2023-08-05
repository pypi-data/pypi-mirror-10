Schematec
=========

.. image:: https://travis-ci.org/mylokin/redisext.svg?branch=master
   :target: https://travis-ci.org/mylokin/redisext

Schematec is a set of tools that brings some static typing into Python and
makes input data validation easier. The purpose of this code is attempt to
bring simplicity to applications logics using separation of data validation
and actual data processing.

Concepts
--------

Schematec separates concept of validation and concept of types casting.

Object deconstruction seems reasonable useful for input data filtering.

Workflow
--------

Schematec determine validity of data using following criterias:

#. Existence (schema validator)
#. Type (converter)
#. Suitability (validator)

Example:

.. code:: python

   a = string and email and required

   ### Cases

   {'a': 'mylokin@me.com'}  # valid
   {'a': 'mylokin'}  # invalid by suitability
   {'a': ''}  # invalid by suitability
   {'a': 1}  # invalid by suitability
   {'a': None}  # invalid by type
   {'a': []}  # invalid by type
   {}  # invalid by existence

   a = string and email

   ### Cases

   {'a': 'mylokin@me.com'}  # valid
   {'a': 'mylokin'}  # invalid by suitability
   {'a': ''}  # invalid by suitability
   {'a': 1}  # invalid by suitability
   {'a': None}  # invalid by type
   {'a': []}  # invalid by type
   {}  # valid

   a = string

   ### Cases

   {'a': 'mylokin@me.com'}  # valid
   {'a': 'mylokin'}  # valid
   {'a': ''}  # valid
   {'a': 1}  # valid
   {'a': None}  # invalid by type
   {'a': []}  # invalid by type
   {}  # valid


Glossary
========

Validator

   Configurable object that checks object for predefined conditions.

Converter

   Converter casts input object to required type if possible.

Schema

   Set of validators

Validation

   Checking process where every value validated through set of validators.

Validators
==========

Required -- any

   Required value, (everything is optional by default).

Regex (URL, Email, IPAddress) -- string

    String contains expected value.

Range -- integer

    Integer within range

Length -- string, array, dictionary

    Length of iteratable is appropriate.

Supported Data Types
====================

Schematec supports subset of JSON data types:

Basic types:

- integer(int)
- string(str)
- boolean(bool)

Containers:

- array(list)
- dictionary(dict)

Extended Data Types
===================

- datetime - based on str
- regexp str - based on str

Order of schema check
=====================

#. Unbound Validators
#. Converters
#. Bound Validators
