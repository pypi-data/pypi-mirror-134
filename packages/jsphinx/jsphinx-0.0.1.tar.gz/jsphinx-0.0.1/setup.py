#
#  JSphinx
#  Java documentation for Python Sphinx.
#  Copyright Patrick Huang 2022
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import setuptools

with open("README.md", "r") as fp:
    long_description = fp.read()

with open("requirements.txt", "r") as fp:
    requirements = fp.read().split("\n")


setuptools.setup(
    name="jsphinx",
    version="0.0.1",
    author="Patrick Huang",
    author_email="huangpatrick16777216@gmail.com",
    description="Java documentation for Python Sphinx.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/phuang1024/jsphinx",
    py_modules=["jsphinx"],
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
