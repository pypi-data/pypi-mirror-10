easysetup
=========

Description, features and To do
-------------------------------

**Description**

*easysetup* helps creating a package distribution setup, that also runs tests and creates HTML and PDF documentation, in Windows.

After installation you should edit easysetup.py (where it was installed) to update the default values for DEFAULT_AUTHOR, DEFAULT_EMAIL, DEFAULT_URL, DEFAULT_VERSION and DEFAULT_LICENSE.

When running easysetup without options, everything on the current directory is moved to a _bak directory.

After running easysetup, you can find a build.cmd in the current directory that should be run to build your application (execute build -h to see usage options).

**Features:**

* Easy to use, just run easysetup from your application setup directory (it backups everything in current directory to _bak directory when run without options).
* Allows creating source, wheel, win (exe or msi), py2exe, egg, dumb (zip on windows, tar/ztar/gztar/zip on GNU Linux in the future) and rpm (on GNU Linux in the future) dists.
* All setup configuration is in one file (appinfo.py).
* Runs tests and creates HTML and PDF documentation (if you have them, of course).
* Can publish to PyPI (including documentation if exists) and PyPI tests.

* Creates index.html with redirection to RTD, to be used if preferred for hosting documentation.
* Creates templates for Travis, Shippable and tox.
* Creates a template for development requirements.
* Creates a template for installation requirements.
* Creates a template for git VCS exceptions.
* Creates a template for files to be included in the setup.
* Creates a template for a README file.
* Creates a template for wheel setup and Sphinx documentation upload.
* Can create template files in the doc directory (assumes use of Sphinx and that the sphinx-quickstart command was already executed).
* Can create an updated reference.rst in the doc directory (assumes previous item with the autodoc extension).
* Updates usage section in README.rst based on usage.txt, if it exists inside your application directory.

**To do**

* correct py2exe to include subdirs (doc and template).
* Add appveyor templates.
* Auto rebuild doc/reference.rst on each dist build.
* Auto rebuild requirements.txt on each dist build.
* Change easysetup from Windows only to universal (move build.cmd functionality to easysetup.py).
* py2exe in Py3.
* CXF in Py2 and Py3.
* Checks and error messages.


Installation, usage and options
-------------------------------

**Installation**

.. code:: bash

    $ pip install easysetup

Edit easysetup.py (where it was installed) to update the default values for DEFAULT_AUTHOR, DEFAULT_EMAIL, DEFAULT_URL, DEFAULT_VERSION and DEFAULT_LICENSE.

**Usage**

.. code:: bash

    $ easysetup

**Options**

.. code:: bash

    $ easysetup -h
    usage: easysetup [-option]

    optional arguments:
      -d, --doc             creates template files in the doc directory
      -h, --help            show this help message
      -l, --license         show license
      -r, --reference       creates an updated reference.rst in the doc directory
      -V, --version         show version

    No arguments creates setup files.
    easysetup should always be run from the application setup directory.

Resources and contributing
--------------------------

**Resources**

* `Repository <https://github.com/jcrmatos/easysetup>`_

**Contributing**

1. Fork the `repository`_ on GitHub.
2. Make a branch of master and commit your changes to it.
3. Ensure that your name is added to the end of the AUTHORS.rst file using the format:
   ``Name <email@domain.com>``
4. Submit a Pull Request to the master branch on GitHub.

.. _repository: https://github.com/jcrmatos/easysetup

Copyright 2009-2015 Joao Carlos Roseta Matos. Licensed under the GNU General Public License v2 or later (GPLv2+).


