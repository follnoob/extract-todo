#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 - 2021 Jens Wilberg
#
# This file is part of extract_todo.
#
# extract_todo is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# extract_todo is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with extract_todo.  If not, see <http://www.gnu.org/licenses/>.
"""Tests for 'extract_todo'."""
import sys
from pathlib import Path

from pyfakefs.fake_filesystem_unittest import TestCase

# Import module to test
sys.path.append(str(Path(__file__).resolve().parent.parent.joinpath("src")))
from extract_todo.parser.parser_factory import ParserFactory, PythonParser, LatexParser, DefaultParser  # noqa: E402


class Test(TestCase):
    """Tests for 'extract_todo' package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.setUpPyfakefs()

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    def test_ParserFactory_create_PythonParser(self):
        parser_factory = ParserFactory()
        fpath = Path("test.py")
        parser = parser_factory.create(fpath)
        assert isinstance(parser, PythonParser)

    def test_ParserFactory_create_LatexParser(self):
        parser_factory = ParserFactory()
        fpath = Path("test.tex")
        parser = parser_factory.create(fpath)
        assert isinstance(parser, LatexParser)

    def test_ParserFactory_create_DefaultParser(self):
        parser_factory = ParserFactory()
        fpath = Path("test.cpp")
        parser = parser_factory.create(fpath)
        assert isinstance(parser, DefaultParser)

    def test_ParserFactory_create_dir(self):
        parser_factory = ParserFactory()
        fpath = Path(".")
        try:
            parser_factory.create(fpath)
        except ValueError as e:
            assert str(e) == "'.' is a folder!"
        else:
            assert False, "Expected ValueError"

    def test_ParserFactory_create_unsupported_file_type(self):
        parser_factory = ParserFactory()
        fpath = Path("test.zzz")
        try:
            parser_factory.create(fpath)
        except ValueError as e:
            assert str(e) == "'.zzz'-files are not supported!"
        else:
            assert False, "Expected ValueError"
