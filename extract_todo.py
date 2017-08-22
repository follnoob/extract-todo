#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Jens Wilberg
#
# extract_todo.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# extract_todo.py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with extract_todo.py.  If not, see <http://www.gnu.org/licenses/>.
"""Tool for extracting TODOs from text/sorce files.

Currently only 'utf-8' file-encoding is supported.
"""
import codecs
import os
import argparse

__version__ = "0.1.0"

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


def argparser_conf():
    """Configuration for argparser.

    Returns
    -------
    ArgumentParser
        returns the ergumentparser
    """
    parser = argparse.ArgumentParser(description="Extracts TODOs from a given file.\
        TODOs are only recognized, if there are at the beginning of a single \
        line comment. Supported files are LaTex tex-files and Python-files. \
        Currently only 'utf-8' file-encoding is supported.")
    parser.add_argument("fname", metavar="FILENAME", help="Path to file.")
    return parser


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
    with codecs.open(fname, "r", "utf-8") as f:
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


def main():
    """Main-function."""
    parser = argparser_conf()
    args = parser.parse_args()
    fname = args.fname
    try:
        todos = extract_todos(fname)
    except KeyError:
        ext = os.path.splitext(fname)
        print("%s-files are not supported!" % ext[1])
        exit(1)
    if todos:
        print('\n'.join(todos))
    else:
        print("There are no TODOs.")


if __name__ == '__main__':
    main()
