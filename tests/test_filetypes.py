#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 - 2019 Jens Wilberg
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
import unittest
import os
import extract_todo


class Test(unittest.TestCase):
    """Tests for 'extract_todo' package."""

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
        fpath = os.path.join(self.path, "test.tex")
        corr = [(fpath, 2, "test"), (fpath, 3, "test 2")]
        todos = extract_todo.extract_todos(fpath)
        self.assertListEqual(todos, corr)

    def test_py(self):
        """Test py-file."""
        fpath = os.path.join(self.path, "test.py")
        corr = [(fpath, 1, "test"), (fpath, 5, "test 2")]
        todos = extract_todo.extract_todos(fpath)
        self.assertListEqual(todos, corr)

    def test_h(self):
        """Test h-file."""
        fpath = os.path.join(self.path, "test.h")
        corr = [(fpath, 1, "test"), (fpath, 3, "test 2")]
        todos = extract_todo.extract_todos(fpath)
        self.assertListEqual(todos, corr)

    def test_c(self):
        """Test c-file."""
        fpath = os.path.join(self.path, "test.c")
        corr = [(fpath, 1, "test"), (fpath, 7, "test 2")]
        todos = extract_todo.extract_todos(fpath)
        self.assertListEqual(todos, corr)

    def test_hpp(self):
        """Test hpp-file."""
        fpath = os.path.join(self.path, "test.hpp")
        corr = [(fpath, 1, "test"), (fpath, 3, "test 2")]
        todos = extract_todo.extract_todos(fpath)
        self.assertListEqual(todos, corr)

    def test_cpp(self):
        """Test cpp-file."""
        fpath = os.path.join(self.path, "test.cpp")
        corr = [(fpath, 1, "test"), (fpath, 7, "test 2")]
        todos = extract_todo.extract_todos(fpath)
        self.assertListEqual(todos, corr)

    def test_js(self):
        """Test js-file."""
        fpath = os.path.join(self.path, "test.js")
        corr = [(fpath, 1, "test"), (fpath, 4, "test 2")]
        todos = extract_todo.extract_todos(fpath)
        self.assertListEqual(todos, corr)

    def test_cs(self):
        """Test cs-file."""
        fpath = os.path.join(self.path, "test.cs")
        corr = [(fpath, 1, "test"), (fpath, 7, "test 2")]
        todos = extract_todo.extract_todos(fpath)
        self.assertListEqual(todos, corr)

    def test_go(self):
        """Test go-file."""
        fpath = os.path.join(self.path, "test.go")
        corr = [(fpath, 5, "test"), (fpath, 7, "test 2")]
        todos = extract_todo.extract_todos(fpath)
        self.assertListEqual(todos, corr)

    def test_java(self):
        """Test java-file."""
        fpath = os.path.join(self.path, "test.java")
        corr = [(fpath, 1, "test"), (fpath, 4, "test 2")]
        todos = extract_todo.extract_todos(fpath)
        self.assertListEqual(todos, corr)

    def test_ruby(self):
        """Test ruby-file."""
        fpath = os.path.join(self.path, "test.rb")
        corr = [(fpath, 1, "test"), (fpath, 2, "test 2")]
        todos = extract_todo.extract_todos(fpath)
        self.assertListEqual(todos, corr)
