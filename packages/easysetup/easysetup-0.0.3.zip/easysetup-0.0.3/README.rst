easysetup
=========

*easysetup* helps creating a package distribution setup, while running tests creating HTML and PDF documentation, in Windows.

**Features:**

* Easy to use, just run easysetup from your application setup directory. It can be empty.
* It allows creating source, egg, wheel, win and py2exe dists.
* All setup configuration is in one file (appinfo.py).
* It runs tests and creates HTML and PDF documentation (if you have them, of course).
* It creates templates for Travis, Shippable and tox.
* It creates a template for development requirements.
* It creates an empty template for installation requirements.
* It creates a template for git VCS exceptions.
* It creates a template for files to be included in the setup.
* It creates a template for a README file.
* It creates a template for wheel setup and Sphinx documentation upload.
* It can create template files in the doc directory (assumes use of Sphinx 1.3.1+ and that the sphinx-quickstart command was already executed).
* It can create an updated reference.rst in the doc directory (assumes previous item with the autodoc extension).

After running easysetup, you can find a build.cmd in the current directory that should be run to build your application (check the comments inside the file for usage).

When running easysetup without options, if there are any files on the current directory, they are moved to a _bak directory.

To do
-----

* Sync README.rst and usage.txt.
* Add appveyor templates.
* py2exe in Py3.
* CXF in Py2 and Py3.
* Checks and error messages.

Installation
------------

.. code:: bash

    $ pip install easysetup

Usage
-----

.. code:: bash

    $ easysetup

Options
-------

.. code:: bash

    $ easysetup -h
    usage: easysetup [-option]

    optional arguments:
      -d, --doc             creates template files in the doc directory
      -h, --help            show this help message
      -l, --license         show license
      -r, --reference       creates an updated reference.rst in the doc directory
      -v, --version         show version

    No arguments creates setup files.
    easysetup should always be run from the application setup directory.

Resources
---------

* `Repository <https://github.com/jcrmatos/easysetup>`_

Contributing
------------

1. Fork the `repository`_ on GitHub.
2. Make a branch of master and commit your changes to it.
3. Ensure that your name is added to the end of the AUTHORS.rst file using the format:
   ``Name <email@domain.com>``
4. Submit a Pull Request to the master branch on GitHub.

.. _repository: https://github.com/jcrmatos/easysetup

