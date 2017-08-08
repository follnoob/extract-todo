# extract-todo

extract-todo is a simple commandline script for the extraction of TODOs.
It can extract TODOs from single-line-comments like:

    # TODO something todo

or

    #TODO something todo

It prints the file, line number and the TODO text.

## installation
You need python3+ to run this script. It is no installation required but you
can install it with

    python setup.py install

## usage

You can use this script with the command

    python extract_todo.py /path/to/file

or after installation

    extract-todo /path/to/file

It prints the filename, line number and the TODO text.


## Author and License

Copyright (C) Jens Wilberg July 2017

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