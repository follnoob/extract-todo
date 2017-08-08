#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Jens Wilberg
#
# This file is part of extract_todo.py.
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
"""Tests for 'extract_todo.py'."""
import unittest
import os
import extract_todo


class Test(unittest.TestCase):
    """Tests for 'extract_todo.py' package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        tmp = os.path.dirname(os.path.realpath(__file__))
        self.path = os.path.join(tmp, "files")
        pass

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    def test_latex(self):
        """Test tex-file."""
        corr = ["test.tex:2\n\ttest", "test.tex:3\n\ttest 2"]
        todos = extract_todo.extract_todos(
            os.path.join(self.path, "test.tex"))
        self.assertListEqual(todos, corr)

    def test_py(self):
        """Test py-file."""
        corr = ["test.py:1\n\ttest", "test.py:5\n\ttest 2"]
        todos = extract_todo.extract_todos(
            os.path.join(self.path, "test.py"))
        self.assertListEqual(todos, corr)

    def test_h(self):
        """Test h-file."""
        corr = ["test.h:1\n\ttest", "test.h:3\n\ttest 2"]
        todos = extract_todo.extract_todos(
            os.path.join(self.path, "test.h"))
        self.assertListEqual(todos, corr)

    def test_c(self):
        """Test c-file."""
        corr = ["test.c:1\n\ttest", "test.c:7\n\ttest 2"]
        todos = extract_todo.extract_todos(
            os.path.join(self.path, "test.c"))
        self.assertListEqual(todos, corr)

    def test_hpp(self):
        """Test hpp-file."""
        corr = ["test.hpp:1\n\ttest", "test.hpp:3\n\ttest 2"]
        todos = extract_todo.extract_todos(
            os.path.join(self.path, "test.hpp"))
        self.assertListEqual(todos, corr)

    def test_cpp(self):
        """Test cpp-file."""
        corr = ["test.cpp:1\n\ttest", "test.cpp:7\n\ttest 2"]
        todos = extract_todo.extract_todos(
            os.path.join(self.path, "test.cpp"))
        self.assertListEqual(todos, corr)

    def test_js(self):
        """Test js-file."""
        corr = ["test.js:1\n\ttest", "test.js:4\n\ttest 2"]
        todos = extract_todo.extract_todos(
            os.path.join(self.path, "test.js"))
        self.assertListEqual(todos, corr)
