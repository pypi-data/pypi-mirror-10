Give a comatibility for following paramstyles to sqlite3 module.

* ANSI C printf format codes, e.g. ...WHERE name=%s
* Python extended format codes, e.g. ...WHERE name=%(name)s

Requirements
------------
* Python 2.7 or 3.4

Setup
-----
::

   $ easy_install sqlite3paramstyle

or

::

   $ pip install sqlite3paramstyle


Usage
-----
::

    import sqlite3paramstyle
    conn = sqlite3paramstyle.connect(":memory:")


History
-------
0.0.2 (2015-07-03)
~~~~~~~~~~~~~~~~~~
* wheel support

0.0.1 (2015-03-30)
~~~~~~~~~~~~~~~~~~
* first release



