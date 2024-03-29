#
# Copyright (C) 2017 - 2021 Jens Wilberg <jens_wilberg@outlook.com>
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
from pathlib import Path
from typing import List, Tuple


class DefaultParser:
    """Defaultparser class.

    This class represents a default parser, which can parse all files with '//'
    as single line comment chars.

    Parameters
    ----------
    fpath : Path
        filename
    """

    def __init__(self, fpath: Path):
        self._comment = "//"
        self._file = fpath

    def parse(self) -> List[Tuple[Path, int, str]]:
        """Parse file for comments.

        Returns
        -------
        list of tuple
            List of tuples. the tuples have the form
            (filename, linenumber, string)
        """
        comments = []
        size = len(self._comment)
        with self._file.open("r") as f:
            for line, text in enumerate(f, 1):
                match = re.search(rf"{self._comment}.+", text)
                if match:
                    comment = match.group(0)[size:].strip()
                    comments.append((self._file, line, comment))

        return comments
