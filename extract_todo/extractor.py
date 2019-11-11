# Copyright (C) 2017 - 2019 Jens Wilberg <jens_wilberg@outlook.com>
#
# This file is part of extract-todo.
#
# extract-todo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# extract-todo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with extract-todo.  If not, see <http://www.gnu.org/licenses/>.
"""Tool for extracting TODOs from text/source files.

Currently only 'utf-8' file-encoding is supported.
"""
import re

from .parser import ParserFactory


def extract_todos(fname):
    """Method for TODO extraction.

    Parameters
    ----------
    fname : str
        Path to file.

    Returns
    -------
    list of str
        List with TODOs.

    """
    factory = ParserFactory()
    parser = factory.create(fname)
    todos = []
    for comment in parser.parse():
        match = re.search(r"TODO[ |\t]*(.*)$", comment[2])
        if match:
            todos.append("{}:{}\n\t{}".format(
                comment[0], comment[1], match.group(1)))
    return todos
