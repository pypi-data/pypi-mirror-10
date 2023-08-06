# Yith Library Server is a password storage server.
# Copyright (C) 2012-2013 Yaco Sistemas
# Copyright (C) 2012-2013 Alejandro Blanco Escudero <alejandro.b.e@gmail.com>
# Copyright (C) 2012-2015 Lorenzo Gil Sanchez <lorenzo.gil.sanchez@gmail.com>
#
# This file is part of Yith Library Server.
#
# Yith Library Server is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Yith Library Server is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Yith Library Server.  If not, see <http://www.gnu.org/licenses/>.

import os
import platform
import sys

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()


def parse_requirements():
    """Parses requirements.txt file into a dictionary.

    requirements.txt should be structuctured in sections. Each section
    should begin with a comment and the name of the section. E.g.:

    # base #
    package1
    package2==1.0

    # other #
    package3<=4.2

    Then the packages per section can be accessed like this:

    >>> requirements = parse_requirements()
    >>> requirements['base']
    ['package1', 'package2==1.0']
    >>> requirements['other']
    ['package3<=4.2']
    >>> requirements['all']
    ['package1', 'package2==1.0', 'package3<=4.2']

    """
    requirements = {}
    all_requirements = []

    with open('requirements.txt', 'r') as requirements_file:
        current_section = None
        for line in requirements_file:
            line = line.strip()
            if line.startswith('#') and line.endswith('#'):
                current_section = line.strip('#').strip()
                requirements[current_section] = []
                continue

            # remove inline comments
            if '#' in line:
                line = line[:line.index('#')]
                line = line.strip()

            if line:
                if current_section is not None:
                    requirements[current_section].append(line)
                all_requirements.append(line)

    requirements['all'] = all_requirements

    return requirements

requirements = parse_requirements()

if sys.version_info[0] < 3:
    # packages that only work in Python 2.x
    requirements['base'].extend(requirements['python2'])

if platform.python_implementation() == 'PyPy':
    requirements['base'].extend(requirements['pypy'])
    requirements['base'].remove('psycopg2==2.6')


setup(
    name='yith-library-server',
    version='0.3',
    description='yith-library-server',
    long_description=README + '\n\n' +  CHANGES,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pyramid",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements['base'],
    tests_require=requirements['base'] + requirements['test support'],
    extras_require = {
        'testing': requirements['testing'] + requirements['test support'],
        'docs': requirements['docs'],
    },
    test_suite="yithlibraryserver",
    entry_points = """\
    [paste.app_factory]
    main = yithlibraryserver:main
    [console_scripts]
    yith_users_report = yithlibraryserver.scripts.reports:users
    yith_apps_report = yithlibraryserver.scripts.reports:applications
    yith_stats_report = yithlibraryserver.scripts.reports:statistics
    yith_migrate = yithlibraryserver.scripts.migrations:migrate
    yith_send_backups_via_email = yithlibraryserver.scripts.backups:send_backups_via_email
    yith_announce = yithlibraryserver.scripts.announce:announce
    yith_build_assets = yithlibraryserver.scripts.buildassets:buildassets
    yith_create_db = yithlibraryserver.scripts.createdb:createdb
    yith_mongo2postgres = yithlibraryserver.scripts.mongo2postgres:mongo2postgres""",
)
