#
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
"""This module contains the default parser for files."""
import re


class DefaultParser:
    """Defaultparser class.

    This class represents a default parser, which can parse all files with '//'
    as single line comment chars.

    Parameters
    ----------
    fname : str
        filename
    """

    def __init__(self, fname: str):
        self._comment = r"//.+"
        self._file = fname

    def parse(self) -> list:
        """Parse file for comments.

        Returns
        -------
        list of tuple
            List of tuples. the tuples have the form
            (filename, linenumber, string)
        """
        comments = []
        with open(self._file, "r") as f:
            for line, text in enumerate(f, 1):
                match = re.search(self._comment, text)
                if match:
                    comment = match.group(0)[2:].strip()
                    comments.append((self._file, line, comment))

        return comments
