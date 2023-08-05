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

"""Setup for py2exe."""

# Python 3 compatibility
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
# sometimes py2exe requires the following import to be commented in this file
# or in this file and appinfo
from __future__ import unicode_literals

import glob
import os
import sys

import setuptools
import py2exe  # must be after setuptools

import appinfo


DESC = LONG_DESC = ''
if os.path.isfile(appinfo.README_FILE):
    with open(appinfo.README_FILE) as file_:
        LONG_DESC = file_.read()
        DESC = LONG_DESC.split('\n')[3]

#PACKAGES = [appinfo.APP_NAME]  # use only if find_packages() doesn't work

REQUIREMENTS = ''
if os.path.isfile(appinfo.REQUIREMENTS_FILE):
    with open(appinfo.REQUIREMENTS_FILE) as file_:
        REQUIREMENTS = file_.read().splitlines()

PATH = appinfo.APP_NAME + '/'
SCRIPT = PATH + appinfo.APP_NAME + '.py'
DATA_FILES_PY2EXE = [('', glob.glob(PATH + '*.txt'))]

OPTIONS = {'py2exe': {'compressed': True,
                      'ascii': False,
                      #'packages': ['colorama'],
                      #'bundle_files': 1,  # exe does not work
                      #'includes': ['colorama'],
                      #'excludes': ['doctest', 'pdb', 'unittest', 'difflib',
                      #             'inspect', 'pyreadline', 'optparse',
                      #             'calendar', 'email', '_ssl',
                      #             # 'locale', 'pickle'
                      #            ]
                     }
          }

# add modules_dir to PYTHONPATH so all modules inside it are included
# in py2exe library
sys.path.insert(1, appinfo.APP_NAME)

setuptools.setup(name=appinfo.APP_NAME,
                 version=appinfo.APP_VERSION,
                 description=DESC,
                 long_description=LONG_DESC,
                 license=appinfo.LICENSE,
                 url=appinfo.URL,
                 author=appinfo.AUTHOR,
                 author_email=appinfo.AUTHOR_EMAIL,

                 classifiers=appinfo.CLASSIFIERS,
                 keywords=appinfo.KEYWORDS,

                 packages=setuptools.find_packages(),
                 #packages=setuptools.find_packages(exclude=['docs',
                 #                                           'tests*']),

                 # use only if find_packages() doesn't work
                 #packages=PACKAGES,
                 #package_dir={'': appinfo.APP_NAME},

                 install_requires=REQUIREMENTS,

                 # used only if the package is not in PyPI, but exists as an
                 # egg, sdist format or as a single .py file
                 # see http://peak.telecommunity.com/DevCenter/setuptools#dependencies-that-aren-t-in-pypi
                 #dependency_links = ['http://host.domain.local/dir/'],

                 console=[SCRIPT],
                 options=OPTIONS,
                 data_files=DATA_FILES_PY2EXE,
                 #windows=[{'script': appinfo.APP_NAME + '.py',
                 #          'icon_resources': [(0, appinfo.APP_NAME + '.ico')]
                 #         }],
                )
