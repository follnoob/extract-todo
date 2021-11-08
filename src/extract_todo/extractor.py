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
"""Tool for extracting TODOs from text/source files.

Currently only 'utf-8' file-encoding is supported.
"""
import re
from pathlib import Path
from typing import List, Tuple

from .parser import ParserFactory


def extract_todos(fpath: Path) -> List[Tuple[Path, int, str]]:
    """Method for TODO extraction.

    Parameters
    ----------
    fpath : Path
        Path to file.

    Returns
    -------
    list of tuple
        List with TODOs.

    """
    factory = ParserFactory()
    parser = factory.create(fpath)
    todos = []
    for _, line, text in parser.parse():
        match = re.search(r"TODO[ |\t]*(.*)$", text)
        if match:
            todos.append((fpath, line, match.group(1)))
    return todos


class Printer:
    """Pretty print todos.

    This class formats the todos into a pretty string for printing. The string
    has the following format:

    ```shell
    path/to/file
        LINE 1:     text
        LINE 5:     more text
    ```

    Parameter
    ---------
    todos : list
        list of todo tuples with the format (filepath, linenumber, text)
    """

    def __init__(self, todos: List[Tuple[Path, int, str]]):
        self._todos = todos

    def __str__(self):
        """Transform todo list to printable string."""
        lines = ""
        filepath = ""
        for fpath, line, text in self._todos:
            filepath = str(fpath)
            lines += "  LINE {}:\t{}\n".format(line, text)
        return "{}\n{}".format(filepath, lines)
