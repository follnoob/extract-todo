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
"""This module contains the parser for python files."""
from pathlib import Path

from .default_parser import DefaultParser


class PythonParser(DefaultParser):
    """Parser class for python files.

    Parameters
    ----------
    fpath : Path
        filename
    """

    def __init__(self, fpath: Path):
        self._comment = r"#.+"
        self._file = fpath
