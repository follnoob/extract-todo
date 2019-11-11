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
import os

# GLOBALS
_FILES = {
    # Dict with supproted files and their comment chars
    ".tex": '%',
    ".py": '#',
    ".h": "//",
    ".c": "//",
    ".hpp": "//",
    ".cpp": "//",
    ".js": "//"
}


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
    global _FILES
    ext = os.path.splitext(fname)
    comm_char = _FILES[ext[1]]
    todos = []
    with open(fname, "r") as f:
        lineCount = 0
        for line in f:
            lineCount += 1
            if comm_char not in line:
                continue
            try:
                line = line.split(comm_char, 1)[1].strip()
            except IndexError:
                pass
            if line.startswith("TODO"):
                todo = line.split("TODO", 1)[1].strip()
                todos.append("%s:%d\n\t%s" %
                             (os.path.basename(fname), lineCount, todo))
    return todos
