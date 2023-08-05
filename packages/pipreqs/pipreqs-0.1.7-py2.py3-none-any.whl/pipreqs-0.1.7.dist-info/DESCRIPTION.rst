===============================
``pipreqs`` - Generate requirements.txt file for any project based on imports
===============================

.. image:: https://img.shields.io/travis/bndr/pipreqs.svg
        :target: https://travis-ci.org/bndr/pipreqs

.. image:: https://img.shields.io/pypi/v/pipreqs.svg
        :target: https://pypi.python.org/pypi/pipreqs

Installation
------------

::

    pip install pipreqs

Usage
-----

::

    Usage:
        pipreqs <path> [options]

    Options:
    	--savepath Supply custom path for requirements.txt
        --debug    See debug output

Example
-------

::

    $ pipreqs /home/project/location
    Looking for imports
    Getting latest version of packages information from PyPi
    Found third-party imports: flask, requests, sqlalchemy, docopt
    Successfuly saved requirements file in: /home/project/location/requirements.txt

Why not pip freeze?
-------------------

- ``pip freeze`` only saves the packages that are installed with ``pip install`` in your environment. 
- pip freeze saves all packages in the environment including those that you don't use in your current project. (if you don't have virtualenv)
- and sometimes you just need to create requiremetns.txt for a new project without installing modules.




History
-------

0.1.7 (2015-04-24)
---------------------

* Add more assertions in tests
* Add more verbose output
* Add recursive delete to Makefile clean
* Update Readme

0.1.6 (2015-04-22)
---------------------

* py3 print function

0.1.5 (2015-04-22)
---------------------

* Add Readme, Add Examples
* Add Stdlib into package

0.1.1 (2015-04-22)
---------------------

* Fix regex matching for imports
* Release on Pypi

0.1.0 (2015-04-22)
---------------------

* First release on Github.


