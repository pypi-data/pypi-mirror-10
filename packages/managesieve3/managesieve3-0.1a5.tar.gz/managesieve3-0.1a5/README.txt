============
managesieve3
============

Overview
========

A pure Python client implementation of "A Protocol for Remotely
Managing Sieve Scripts", as defined in RFC-5804. It works with either
Python 2.7 or Python 3.3+.

Module Contents
===============

class Managesieve
-----------------

The main class for interactive with sieve server.

Exceptions
----------

BaseException
*************

The base class for all exceptions raised by managesieve3.

ServerResponseNo
****************

The sieve server sent a NO response. See RFC-5804 for details.

Available fields are:

+-----------+------------------------------------------------------+
| Name      | Description                                          |
+-----------+------------------------------------------------------+
| `name`    | The name of the RFC-5804 command that was being      |
|           | executed when the server returned a NO response.     |
+-----------+------------------------------------------------------+
| `code`    | The code returned in the NO response. This is a      |
|           | list (possibly of length 1) of the heirarchical      |
|           | response codes.                                      |
+-----------+------------------------------------------------------+
| `text`    | The human readable text error message, if any.       |
+-----------+------------------------------------------------------+
| `results` | The textual body of the response, if any.            |
+-----------+------------------------------------------------------+


ServerResponseBye
*****************

The sieve server sent a BYE response. See RFC-5804 for details.

Available fields are:

+-----------+------------------------------------------------------+
| Name      | Description                                          |
+-----------+------------------------------------------------------+
| `name`    | The name of the RFC-5804 command that was being      |
|           | executed when the server returned a BYE response.    |
+-----------+------------------------------------------------------+
| `code`    | The code returned in the BYE response. This is a     |
|           | list (possibly of length 1) of the heirarchical      |
|           | response codes.                                      |
+-----------+------------------------------------------------------+
| `text`    | The human readable text error message, if any.       |
+-----------+------------------------------------------------------+
| `results` | The textual body of the response, if any.            |
+-----------+------------------------------------------------------+

ServerProtocolError
*******************

The client code detected a protocol error when talking to the sieve
server.
