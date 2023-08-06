#
# setup.py
#
# Copyright (C) 2021 Franco Masotti (franco DoT masotti {-A-T-} tutanota DoT com)
#
# This file is part of licheck.
#
# licheck is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# licheck is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with licheck.  If not, see <http://www.gnu.org/licenses/>.
#
r"""setup.py."""

from setuptools import find_packages, setup

setup(
    name='licheck',
    version='1.0.0',
    packages=find_packages(exclude=['*tests*']),
    license='GPL',
    description='Automatically check the licenses of package dependencies.',
    long_description=open('README.rst').read(),
    long_description_content_type='text/x-rst',
    package_data={
        '': ['*.txt', '*.rst'],
    },
    author='Franco Masotti',
    author_email='franco.masotti@tutanota.com',
    keywords='text license',
    url='https://blog.franco.net.eu.org/software/#licheck',
    python_requires='>=3.5, <4',
    entry_points={
        'console_scripts': [
            'licheck=licheck.__main__:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Utilities',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
    ],
    install_requires=[
        'PyYAML>=6,<7',
        'tabulate>=0,<1',
        'appdirs>=1,<2',
        'requests>=2.26,<2.27',
    ],
)
