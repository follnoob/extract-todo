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
import os
import unittest

import extract_todo
from pyfakefs.fake_filesystem_unittest import Patcher


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

    def extract_todo(self, file, content, expected):
        """DOCSTRING."""
        with Patcher() as patcher:
            patcher.fs.create_file(file, contents=content)
            todos = extract_todo.extract_todos(file)
            self.assertListEqual(todos, expected)

    def test_latex(self):
        """Test tex-file."""
        content = """\
\\begin{{document}}
% TODO test
Test % TODO test 2
\\end{{document}}
"""
        fpath = os.path.join(self.path, "test.tex")
        corr = [(fpath, 2, "test"), (fpath, 3, "test 2")]

        self.extract_todo(fpath, content, corr)

    def test_py(self):
        """Test py-file."""
        content = """\
# TODO test

def main():
    print("Hello World")  # TODO test 2


if __name__ == '__main__':
    main()
"""
        fpath = os.path.join(self.path, "test.py")
        corr = [(fpath, 1, "test"), (fpath, 4, "test 2")]

        self.extract_todo(fpath, content, corr)

    def test_h(self):
        """Test h-file."""
        content = """\
//TODO test

#include <stdio.h> //TODO test 2
"""
        fpath = os.path.join(self.path, "test.h")
        corr = [(fpath, 1, "test"), (fpath, 3, "test 2")]

        self.extract_todo(fpath, content, corr)

    def test_c(self):
        """Test c-file."""
        content = """\
// TODO test

#include <test.h>

int main()
{
    printf("Hello World!"); //TODO test 2
    return 0;
}
"""
        fpath = os.path.join(self.path, "test.c")
        corr = [(fpath, 1, "test"), (fpath, 7, "test 2")]

        self.extract_todo(fpath, content, corr)

    def test_hpp(self):
        """Test hpp-file."""
        content = """\
//TODO test

#include <iostream> //TODO test 2
"""
        fpath = os.path.join(self.path, "test.hpp")
        corr = [(fpath, 1, "test"), (fpath, 3, "test 2")]

        self.extract_todo(fpath, content, corr)

    def test_cpp(self):
        """Test cpp-file."""
        content = """\
// TODO test

#include <test.hpp>

int main()
{
    std::cout << "Hello World!"; //TODO test 2
    return 0;
}
"""
        fpath = os.path.join(self.path, "test.cpp")
        corr = [(fpath, 1, "test"), (fpath, 7, "test 2")]

        self.extract_todo(fpath, content, corr)

    def test_js(self):
        """Test js-file."""
        content = """\
// TODO test

var foo = "Hello World!"
console.log(foo) //TODO test 2
"""
        fpath = os.path.join(self.path, "test.js")
        corr = [(fpath, 1, "test"), (fpath, 4, "test 2")]

        self.extract_todo(fpath, content, corr)

    def test_cs(self):
        """Test cs-file."""
        content = """\
// TODO test
namespace HelloWorld
{
    class Hello {
        static void Main(string[] args)
        {
            System.Console.WriteLine("Hello World!"); // TODO test 2
        }
    }
}
"""
        fpath = os.path.join(self.path, "test.cs")
        corr = [(fpath, 1, "test"), (fpath, 7, "test 2")]

        self.extract_todo(fpath, content, corr)

    def test_go(self):
        """Test go-file."""
        content = """\
package main

import "fmt"

// TODO test
func main() {
    fmt.Println("hello world") // TODO test 2
}
"""
        fpath = os.path.join(self.path, "test.go")
        corr = [(fpath, 5, "test"), (fpath, 7, "test 2")]

        self.extract_todo(fpath, content, corr)

    def test_java(self):
        """Test java-file."""
        content = """\
// TODO test
class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!"); // TODO test 2
    }
}
"""
        fpath = os.path.join(self.path, "test.java")
        corr = [(fpath, 1, "test"), (fpath, 4, "test 2")]

        self.extract_todo(fpath, content, corr)

    def test_ruby(self):
        """Test ruby-file."""
        content = """\
# TODO test
puts 'Hello, world!' # TODO test 2
"""
        fpath = os.path.join(self.path, "test.rb")
        corr = [(fpath, 1, "test"), (fpath, 2, "test 2")]

        self.extract_todo(fpath, content, corr)
