# extract-todo

[![travis](https://travis-ci.org/follnoob/extract-todo.svg?branch=master)](https://travis-ci.org/follnoob/extract-todo)
![Python build](https://github.com/follnoob/extract-todo/workflows/Python%20build/badge.svg)

extract-todo is a simple commandline script for the extraction of TODOs.
It can extract TODOs from single-line-comments like:

```python
    # TODO something todo
```

It prints the file, line number and the TODO text.

## installation


You need python3+ to run this script. It is no installation required but
you can install it with

    python setup.py install

or install it from pypi with

    pip install extract-todo

## usage

You can use this script with the command

    python -m extract_todo /path/to/file

or after installation

    extract-todo /path/to/file

It prints the filename, line number and the TODO text.

## Author and License

Copyright (C) Jens Wilberg July 2021

    extract_todo.py is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    extract_todo.py is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with extract_todo.py.  If not, see <http://www.gnu.org/licenses/>.
