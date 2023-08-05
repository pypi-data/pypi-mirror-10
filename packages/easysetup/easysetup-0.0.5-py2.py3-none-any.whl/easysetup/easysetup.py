#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2009-2015 Joao Carlos Roseta Matos
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Helps creating a package distribution setup for Windows users.

See usage.txt for command line usage.
"""

# Python 3 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import builtins  # Python 3 compatibility
import datetime as dt
#import future  # Python 3 compatibility
import glob
import io  # Python 3 compatibility
import os
import shutil as shu
import sys
import zipfile as zip

import colorama as clrm

import common
import localization as lcl


DEFAULT_AUTHOR = 'CHANGE_ME'
DEFAULT_EMAIL = 'CHANGE_ME'
DEFAULT_URL = 'CHANGE_ME'  # eg. https://github.com/<username>/

DEFAULT_VERSION = '0.0.1'
DEFAULT_LICENSE = 'GNU General Public License v2 or later (GPLv2+)'

BAK_DIR = '_bak'


app_name = ''
app_version = ''
app_license = ''
app_author = ''
app_email = ''
app_url = ''
app_keywords = ''
cur_date = str(dt.date.today())


def update_file(filename):
    """Update file with user input."""
    with io.open(filename, encoding=common.SYS_ENC) as file_:
        text = file_.readlines()

    new_text = ''
    changed = False
    for line in text:
        if 'APPLICATION_NAME' in line:
            line = line.replace('APPLICATION_NAME', app_name)
            changed = True
        if 'APPLICATION_VERSION' in line:
            line = line.replace('APPLICATION_VERSION', app_version)
            changed = True
        if 'APPLICATION_LICENSE' in line:
            line = line.replace('APPLICATION_LICENSE', app_license)
            changed = True
        if 'APPLICATION_AUTHOR' in line:
            line = line.replace('APPLICATION_AUTHOR', app_author)
            changed = True
        if 'APPLICATION_EMAIL' in line:
            line = line.replace('APPLICATION_EMAIL', app_email)
            changed = True
        if 'APPLICATION_URL' in line:
            line = line.replace('APPLICATION_URL', app_url)
            changed = True
        if 'APPLICATION_KEYWORDS' in line:
            line = line.replace('APPLICATION_KEYWORDS', app_keywords)
            changed = True
        if 'CUR_DATE' in line:
            line = line.replace('CUR_DATE', cur_date)
            changed = True
        # quick hacks
        if 'README.rst' in filename and '================' in line:
            line = line.replace('================', '=' * len(app_name))
            changed = True
        if 'reference.rst' in filename and '::::::::::::::::' in line:
            line = line.replace('::::::::::::::::', ':' * len(app_name))
            changed = True
        new_text += line
    if changed:
        with io.open(filename, 'w', encoding=common.SYS_ENC) as file_:
            file_.writelines(new_text)


def get_app_info():
    """Read application info from appinfo.py."""
    global app_name, app_version, app_license, app_author, app_email, \
           app_url, app_keywords

    with io.open(common.APP_INFO_FILENAME, encoding=common.SYS_ENC) as file_:
        text = file_.readlines()
    for line in text:
        if 'APP_NAME = ' in line:
            app_name = line.split("'")[1]
        if 'APP_VERSION = ' in line:
            app_version = line.split("'")[1]
        if 'APP_LICENSE = ' in line:
            app_license = line.split("'")[1]
        if 'APP_AUTHOR = ' in line:
            app_author = line.split("'")[1]
        if 'APP_EMAIL = ' in line:
            app_email = line.split("'")[1]
        if 'APP_URL = ' in line:
            app_url = line.split("'")[1]
        if 'APP_KEYWORDS = ' in line:
            app_keywords = line.split("'")[1]


def update_ref():
    """Creates a new doc/reference.rst for Sphinx autodoc extension."""
    filenames = glob.glob(app_name + '/*.py')
    # remove __init__.py
    filenames = [filename for filename in filenames
                 if '__init__.py' not in filename and
                 'appinfo.py' not in filename]

    if filenames:
        # remove paths
        filenames = [filename.split(os.sep)[-1] for filename in filenames]
        # remove extensions
        filenames = [filename.split('.')[0] for filename in filenames]

        text = 'Reference\n---------\n'

        for filename in filenames:
            text +=  '\n'
            text +=  filename + '\n' + ':' * len(filename) + '\n\n'
            text +=  '.. automodule:: ' + filename + '\n'
            text += '    :members:\n'

        with io.open('doc/reference.rst', 'w',
                     encoding=common.SYS_ENC) as file_:
            file_.writelines(text)


def update_doc():
    """Update doc dir."""
    filenames = glob.glob(common.DATA_PATH + 'template/doc/*')
    # copy template/doc files
    for filename in filenames:
        # if file exists delete it
        if os.path.isfile('doc/' + filename.split(os.sep)[-1]):
            os.remove('doc/' + filename.split(os.sep)[-1])

        shu.copyfile(filename, 'doc/' + filename.split(os.sep)[-1])

    filenames_to_update = ['conf.py', 'reference.rst']

    # delete .pyc files and update files
    filenames = glob.glob('doc/*')
    for filename in filenames:
        if '.pyc' in filename:
            os.remove(filename)
        else:
            if filename.split(os.sep)[-1] in filenames_to_update:
                update_file(filename)

    update_ref()


def create_redir2RTD_zip():
    """Create zip of index.html that redirects pythonhosted to RTD."""
    filename = 'pythonhosted.org/index.html'
    with zip.ZipFile('pythonhosted.org/redir2RTD.zip', 'w') as archive:
        archive.write(filename, filename.split('/')[-1])


def create_setup():
    """Copy files from template and update them with user input."""
    global app_name, app_version, app_license, app_author, app_email, \
           app_url, app_keywords

    while not app_name:
        app_name = builtins.input(lcl.Q_APP_NAME)

    app_version = builtins.input(lcl.Q_APP_VERSION + '[' + DEFAULT_VERSION +
                                 '] ')
    if not app_version:
        app_version = DEFAULT_VERSION

    app_license = builtins.input(lcl.Q_APP_LICENSE + '[' + DEFAULT_LICENSE +
                                 '] ')
    if not app_license:
        app_license = DEFAULT_LICENSE

    app_author = builtins.input(lcl.Q_APP_AUTHOR + '[' + DEFAULT_AUTHOR + '] ')
    if not app_author:
        app_author = DEFAULT_AUTHOR

    app_email = builtins.input(lcl.Q_APP_EMAIL + '[' + DEFAULT_EMAIL + '] ')
    if not app_email:
        app_email = DEFAULT_EMAIL

    app_url = builtins.input(lcl.Q_APP_URL + '[' + DEFAULT_URL + app_name +
                             '] ')
    if not app_url:
        app_url = DEFAULT_URL + app_name

    app_keywords = builtins.input(lcl.Q_APP_KEYWORDS)
    if not app_keywords:
        app_keywords = app_name

    # backup existing files
    backup = False
    filenames = glob.glob('*')
    filenames += glob.glob('.*')
    if filenames:
        backup = True
        os.mkdir(BAK_DIR)
        for filename in filenames:
            dest = BAK_DIR + '/' + filename.split(os.sep)[-1]
            shu.move(filename, dest)

    filenames = glob.glob(common.DATA_PATH + 'template/*')
    filenames += glob.glob(common.DATA_PATH + 'template/.*')
    # remove doc dir
    filenames = [filename for filename in filenames
                 if 'template' + os.sep + 'doc' not in filename]

    # copy files and dirs
    for filename in filenames:
        if os.path.isfile(filename):
            shu.copyfile(filename, filename.split(os.sep)[-1])
        else:
            shu.copytree(filename, filename.split(os.sep)[-1])

    common.sleep(2)

    os.rename('APPLICATION_NAME', app_name)  # rename application dir

    # collect all filenames, including from 1st level subdirs
    filenames = glob.glob('*')
    filenames += glob.glob('.*')
    new_filenames = []
    for filename in filenames:
        if os.path.isdir(filename):
            new_filenames += glob.glob(filename + '/*')
    filenames += new_filenames

    exceptions = ['__init__.py', 'build.cmd', 'requirements.txt',
                  'requirements-dev.txt', 'setup.py', 'setup_py2exe.py',
                  'setup_utils.py',
                 ]

    # delete .pyc files and update files
    for filename in filenames:
        if os.path.isfile(filename):
            if '.pyc' in filename:
                os.remove(filename)
            else:
                if filename.split(os.sep)[-1] not in exceptions:
                    update_file(filename)

    create_redir2RTD_zip()

    if backup:
        # restore py files from backup, but only if they don't already exist
        filenames = glob.glob(BAK_DIR + '/*.py')
        for filename in filenames:
            dest = app_name + '/' + filename.split(os.sep)[-1]
            if not os.path.isfile(dest):
                shu.copyfile(filename, dest)

    print(lcl.REMINDERS)


def main():
    """Process command line args."""
    clrm.init()

    print(common.banner())

    args = sys.argv[1:]
    if args:
        arg0 = args[0]
        if arg0 in ['-d', '--doc']:
            get_app_info()
            update_doc()
        elif arg0 in ['-l', '--license']:
            print(common.license_())
        elif arg0 in ['-h', '--help']:
            print(common.usage())
        elif arg0 in ['-r', '--reference']:
            get_app_info()
            update_ref()
        elif arg0 in ['-V', '--version']:
            print(lcl.VERSION, common.version())
    else:
        create_setup()


if __name__ == '__main__':
    # import doctest
    # doctest.testmod(verbose=True)
    sys.exit(main())


# TODO: add appveyor templates
# TODO: py2exe in Py3
# TODO: CXF in Py2 and Py3
# TODO: checks and error messages
