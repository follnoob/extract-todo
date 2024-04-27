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
from typing import List, Tuple

from pyfakefs.fake_filesystem_unittest import TestCase

# Import module to test
sys.path.append(str(Path(__file__).resolve().parent.parent.joinpath("src")))
from extract_todo import extract_todos  # noqa: E402


class Test(TestCase):
    """Tests for 'extract_todo' package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.setUpPyfakefs()

    def tearDown(self):
        """Tear down test fixtures, if any."""
        pass

    def extract_todo(self, file: Path, content: str, expected: List[Tuple[Path, int, str]], match_regex=""):
        """Test 'extract_todos' function.

        Parameters
        ----------
        file : pathlib.Path
            Test file path
        content : str
            Content of the test file
        expected : List
            List of expected todos
        """
        self.fs.create_file(file, contents=content)
        todos = extract_todos(file, match_regex=match_regex)
        self.assertListEqual(todos, expected)

    def test_latex(self):
        """Test tex-file."""
        content = """\
\\begin{{document}}
% TODO test
Test % TODO test 2
%TODO test 3
\\end{{document}}
"""
        fpath = Path("test.tex")
        corr = [(fpath, 2, "test"), (fpath, 3, "test 2"), (fpath, 4, "test 3")]

        self.extract_todo(fpath, content, corr)

    def test_py(self):
        """Test py-file."""
        content = """\
# TODO test

def main():
    print("Hello World")  # TODO test 2

#TODO test 3

if __name__ == '__main__':
    main()
"""
        fpath = Path("test.py")
        corr = [(fpath, 1, "test"), (fpath, 4, "test 2"), (fpath, 6, "test 3")]

        self.extract_todo(fpath, content, corr)

    def test_py_with_match_regex(self):
        """Test py-file with match_regex."""
        content = """\
# TODO test

def main():
    print("Hello World")  # TODO test 2
    print("Hello World again")  # TODO test 2 again
    print("Hello World!")  # Plain comment

#TODO test 3

if __name__ == '__main__':
    main()
"""
        fpath = Path("test.py")
        corr = [(fpath, 4, "test 2"), (fpath, 5, "test 2 again")]

        self.extract_todo(fpath, content, corr, match_regex="test 2")

    def test_h(self):
        """Test h-file."""
        content = """\
//TODO test

#include <stdio.h> //TODO test 2
"""
        fpath = Path("test.h")
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
        fpath = Path("test.c")
        corr = [(fpath, 1, "test"), (fpath, 7, "test 2")]

        self.extract_todo(fpath, content, corr)

    def test_hpp(self):
        """Test hpp-file."""
        content = """\
//TODO test

#include <iostream> //TODO test 2
"""
        fpath = Path("test.hpp")
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
        fpath = Path("test.cpp")
        corr = [(fpath, 1, "test"), (fpath, 7, "test 2")]

        self.extract_todo(fpath, content, corr)

    def test_js(self):
        """Test js-file."""
        content = """\
// TODO test

var foo = "Hello World!"
console.log(foo) //TODO test 2
"""
        fpath = Path("test.js")
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
        fpath = Path("test.cs")
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
        fpath = Path("test.go")
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
        fpath = Path("test.java")
        corr = [(fpath, 1, "test"), (fpath, 4, "test 2")]

        self.extract_todo(fpath, content, corr)

    def test_ruby(self):
        """Test ruby-file."""
        content = """\
# TODO test
puts 'Hello, world!' # TODO test 2
"""
        fpath = Path("test.rb")
        corr = [(fpath, 1, "test"), (fpath, 2, "test 2")]

        self.extract_todo(fpath, content, corr)
