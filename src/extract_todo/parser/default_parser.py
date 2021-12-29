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
        self._file = fpath
        self._comment = "//"

    def _parse_comment(self, text: str) -> str:
        """Extract single line comment from `text`.

        Parameters
        ----------
        text : str
            String to check

        Returns
        -------
        str
            String containing the comments content. Empty string if there is no comment.
        """
        match = re.search(rf"{self._comment}.*", text)
        if match:
            return match.group(0)[self._comment_size:].strip()
        return ""

    def parse(self) -> List[Tuple[Path, int, str]]:
        """Parse file for comments.

        Returns
        -------
        list of tuple
            List of tuples. the tuples have the form
            (filename, linenumber, string)
        """
        comments = []
        self._comment_size = len(self._comment)

        with self._file.open("r") as f:
            for line, text in enumerate(f, 1):
                comment = self._parse_comment(text)
                comments.append((self._file, line, comment))

        return comments
