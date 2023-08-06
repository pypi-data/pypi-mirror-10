============
managesieve3
============

Overview
========

A pure Python client implementation of "A Protocol for Remotely
Managing Sieve Scripts", as defined in `RFC-5804
<https://tools.ietf.org/html/rfc5804>`_. It works with either Python
2.7 or Python 3.3+.

Module Contents
===============

class Managesieve
-----------------

The main class for interactive with sieve server.

Here are the members of the *Managesive* class. All of these methods
may raise a *ServerResponseNo* or *ServerResponseBye* exception. See
RFC-5804 for details on when *NO* or *BYE* is returned by the server.

*Managesieve(host=None, port=None)*

   If *host* is *None*, it defaults to 'localhost'.  If *port* is
   None, it defaults to 4190.  The connection to the server is
   immediately made. This method may raise any exception raised by the
   *socket* module.

*cmd_authenticate(auth_type, options=None)*

   Send an *AUTHENTICATION* request to the sieve server, along with
   the speficied options, any.  On success, returns None.  If the
   authentication fails, a *ServerResponseNo* exception is raised.

*cmd_capability()*

   Send a *CAPABILITY* request to the sieve server. Returns a list of
   tuples, one per capability returned by the server.

*cmd_checkscript(contents)*

   Send a *CHECKSCRIPT* request to the sieve server. If the contents
   of the script are valid, returns *None*. Otherwise, a
   *ServerResponseNo* exception is raised.

*cmd_deletescript(name)*

   Send a *DELETESCRIPT* request to the sieve server. The script
   *name* is deleted. Returns *None* on success. Raises a
   *ServerResponseNo* if the script cannot be deleted (for example, if
   it does not exist or is the currently active script).

*cmd_getscript(name)*

   Send a *GETSCRIPT* request to the sieve server. On success, the
   contents script named *name* is returned. On error (for example, if
   the script does not exist), a *ServerResponseNo* exception is
   raised.

*cmd_havespace(name, size)*

*cmd_listscripts()*

*cmd_logout()*

*cmd_noop()*

*cmd_putscript(name, contents)*

*cmd_renamescript(oldname, newname)*

*cmd_setactive(name)*

*cmd_starttls(keyfile=None, certfile=None)*

*login_plain(username, authuser, password)*

Exceptions
----------

BaseException
+++++++++++++

The base class for all exceptions raised by managesieve3.

ServerResponseNo
++++++++++++++++

The sieve server sent an unexpected *NO* response. See RFC-5804 for
details.

Available fields are:

+-----------+------------------------------------------------------+
| Name      | Description                                          |
+-----------+------------------------------------------------------+
| *name*    | The name of the RFC-5804 command that was being      |
|           | executed when the server returned a NO response.     |
+-----------+------------------------------------------------------+
| *code*    | The code returned in the NO response. This is a      |
|           | list (possibly of length 1) of the heirarchical      |
|           | response codes.                                      |
+-----------+------------------------------------------------------+
| *text*    | The human readable text error message, if any.       |
+-----------+------------------------------------------------------+
| *results* | The textual body of the response, if any.            |
+-----------+------------------------------------------------------+


ServerResponseBye
+++++++++++++++++


The sieve server sent a *BYE* response. See RFC-5804 for details.

Available fields are:

+-----------+------------------------------------------------------+
| Name      | Description                                          |
+-----------+------------------------------------------------------+
| *name*    | The name of the RFC-5804 command that was being      |
|           | executed when the server returned a BYE response.    |
+-----------+------------------------------------------------------+
| *code*    | The code returned in the BYE response. This is a     |
|           | list (possibly of length 1) of the heirarchical      |
|           | response codes.                                      |
+-----------+------------------------------------------------------+
| *text*    | The human readable text error message, if any.       |
+-----------+------------------------------------------------------+
| *results* | The textual body of the response, if any.            |
+-----------+------------------------------------------------------+

ServerProtocolError
+++++++++++++++++++

The client code detected a protocol error when talking to the sieve
server.
