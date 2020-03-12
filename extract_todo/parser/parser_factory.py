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
"""This module contains the parser factory."""
import os

from .default_parser import DefaultParser
from .python_parser import PythonParser
from .latex_parser import LatexParser


class ParserFactory():

    def __init__(self):
        self._builders = {
            # Files with default parser
            ".h": DefaultParser,     # C/C++
            ".c": DefaultParser,     # C
            ".hpp": DefaultParser,   # C++
            ".cpp": DefaultParser,   # C++
            ".js": DefaultParser,    # Javascript
            ".cs": DefaultParser,    # C#
            ".go": DefaultParser,    # go
            ".java": DefaultParser,  # Java
            # Files with custom parser
            ".tex": LatexParser,     # Latex
            ".py": PythonParser,     # Python
            ".rb": PythonParser      # Ruby
        }

    def create(self, fname: str):
        """Create a appropriated parser for the file."""
        if os.path.isdir(fname):
            raise ValueError("'{}' is a folder!".format(fname))
        file_extension = os.path.splitext(fname)[1]
        builder = self._builders.get(file_extension)
        if not builder:
            raise ValueError(
                "'{}'-files are not supported!".format(file_extension))
        return builder(fname)
