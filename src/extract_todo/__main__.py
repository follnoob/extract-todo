#!/usr/bin/env python3
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
import argparse
from fnmatch import fnmatch
from pathlib import Path
from typing import List, Optional

from git import Repo

from extract_todo.__version__ import VERSION_STRING
from extract_todo.extractor import Printer, extract_todos
from .parser import ParserFactory

__version__ = VERSION_STRING

def get_default_glob_patterns():
    supported_extensions = ParserFactory()._builders.keys()
    default_glob_patterns = ["*" + extension for extension in supported_extensions]
    return default_glob_patterns


def get_files_from_git(glob_patterns: Optional[List[str]] = None):
    if glob_patterns is None:
        glob_patterns = get_default_glob_patterns()

    files = []

    for entry in Repo().commit().tree.traverse():
        if any(fnmatch(entry.abspath, glob_pattern) for glob_pattern in glob_patterns):
            files.append(Path(entry.path))

    return files

def main():
    """Main function as entry point."""
    parser = argparse.ArgumentParser(prog="extract-todo", description="Extracts\
            TODOs from a given file. TODOs are only recognized, if there are at\
            the beginning of a single line comment. Supported files are LaTex\
            tex-files and Python-files. Currently only 'utf-8' file-encoding is\
            supported.")

    parser.add_argument("files", metavar="file", type=Path,
                        help="Path to file. If not given, search through all files in git", nargs='*')
    parser.add_argument("--match-regex", metavar="match_regex", type=str, help="Regex pattern that todos should match")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s {}'.format(__version__))
    parser.add_argument('--filename-pattern', metavar="PATTERN", type=str, action="append",
                        help="Limit search to filenames matching PATTERN. Can be specified multiple times. "
                             "Used only if no files specified.")
    args = parser.parse_args()
    try:
        if len(args.files) == 0:
            files = get_files_from_git(args.filename_pattern)
        else:
           files = args.files

        all_todos = [extract_todos(fname, args.match_regex) for fname in files]
        todos_str = [str(Printer(todos)) for todos in all_todos if todos]
        if todos_str:
            print('\n'.join(todos_str).strip())
        else:
            print("There are no TODOs.")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
