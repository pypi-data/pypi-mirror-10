=======
Chartio
=======

Chartio utilities for providing read-only user local database access.

Version 6.0.1


Introduction
------------
This project permits Chartio customers to provide database access by
opening an SSH reverse tunnel from a Chartio server to the customer
database.

Errors, comments, questions may be sent to support at chartio.com


Requirements
------------
Requires a read-only database role and a local SSH client. Requires JSON
support (Python 2.6 or Python 2.5 and simplejson).

Supported Databases
-------------------
MySQL
Oracle
PostgreSQL
Amazon Redshift


Installation
------------
To install, type::

    $ python setup.py install

To uninstall, remove the files
    chartio_setup
    chartio_connect


Troubleshooting
-------------
The log file
    ~/.chartio.d/logs/chartio_connect.log
contains information about the chartio_connect process.


Documentation
-------------
Further documentation may be found at https://support.chartio.com/docs/index/


Package Contents
----------------
    chartio_setup
        The configuration wizard

    chartio_connect
        A script to keep the SSH tunnel alive


Notable Changes
---------------
Version 6.0.1
- Deprecate chartio_setup

Version 5.0.0
- Add support for PrestoDB
- Remove inline datasource schema refresh. Status can be checked on the website.

Version 4.0.0
- Add support for AmazonRedshift

Version 3.1.0
- Add option to specify the hostname of the database server.

Version 3.0.0
- Backwards incompatible update for new Chartio permissions structure.

Version 2.0.4
- Change the ternary operator to if ... else so that Python 2.4.x does not raise a syntax error.

Version 2.0.3
- Update command-line error handling to work with a MySQL 5.6 Warning

Version 2.0.2
- Copyright, e-mail, and text changes

Version 2.0.1
- Backwards incompatible due to server URL changes

Version 1.1.19
- Correct port type issue

Version 1.1.18
- Specify SSH listen port to override local SSH configuration

Version 1.1.17
- Change domain to chartio.com

Version 1.1.16
- add option to post error information to Chartio

Version 1.1.13
- add Oracle support

Version 1.1.12
- check Chartio version

Version 1.1.7
- permit manual entry of database and readonly user/password

Version 1.1.6
- grant 'SHOW VIEW' access when creating mysql read-only database user
- bug fix for handling of blank database administrator password
