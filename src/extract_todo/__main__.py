#!/usr/bin/env python3
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
import argparse

from extract_todo.__version__ import VERSION_STRING
from extract_todo.extractor import extract_todos, Printer

__version__ = VERSION_STRING


def main():
    """Main function as entry point."""
    parser = argparse.ArgumentParser(prog="extract-todo", description="Extracts\
            TODOs from a given file. TODOs are only recognized, if there are at\
            the beginning of a single line comment. Supported files are LaTex\
            tex-files and Python-files. Currently only 'utf-8' file-encoding is\
            supported.")
    parser.add_argument("files", metavar="file",
                        help="Path to file.", nargs='+')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s {}'.format(__version__))
    args = parser.parse_args()
    try:
        todos = [str(Printer(extract_todos(fname))) for fname in args.files]
        if todos:
            print('\n'.join(todos))
        else:
            print("There are no TODOs.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
