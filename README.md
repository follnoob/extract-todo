# extract-todo

![Python build](https://github.com/follnoob/extract-todo/workflows/Python%20build/badge.svg)

extract-todo is a simple commandline tool for the extraction of TODOs.
It can extract TODOs from single-line-comments like:

```python
    # TODO An example todo for python
```

It prints the file, line number and the TODO text.

## Installation

You can build an installable package with the command

    python -m build

The resulting package can then be installed with

    pip install extract_todo-<version>-py3-none-any.whl

Alternatively you can install `extract-todo` directly from source by running
following command from the root of this project

    pip install

## Usage

You can use this tool with the command

    python -m extract_todo /path/to/file

or

    extract-todo /path/to/file

It prints the filename, line number and the TODO text. Example output:

    .\tests\files\test.py
      LINE 1:       test
      LINE 5:       test 2

### Running on all relevant files in a directory

Note that if you want to run this tool on all the supported files in your
git-managed project, you can run `extract-todo` with no file arguments:

    extract-todo

If you want to limit it to searching certain files, you could do something like this:

    extract-todo --filename-pattern='*.py' --filename-pattern='*.rb'

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
