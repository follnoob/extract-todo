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
"""Tests for the --match-regex command line option."""
import io
import sys
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from unittest import mock

# Import module to test
sys.path.append(str(Path(__file__).resolve().parent.parent.joinpath("src")))
from extract_todo.__main__ import main  # noqa: E402


class MatchRegexOptionTest(unittest.TestCase):
    """An invalid --match-regex must fail cleanly instead of tracebacks."""

    def test_invalid_match_regex_exits_2_with_clean_message(self):
        """Invalid regex: exit code 2, no traceback, names the option."""
        with mock.patch.object(sys, "argv",
                               ["extract-todo", "--match-regex", "[invalid", "some.py"]):
            with redirect_stderr(io.StringIO()) as stderr:
                with self.assertRaises(SystemExit) as ctx:
                    main()
        self.assertEqual(ctx.exception.code, 2)
        self.assertIn("--match-regex", stderr.getvalue())
        self.assertNotIn("Traceback", stderr.getvalue())

    def test_valid_match_regex_is_accepted(self):
        """A valid regex is not rejected by option validation."""
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "some.py"
            target.write_text("# TODO hello\n", encoding="utf-8")
            with mock.patch.object(sys, "argv",
                                   ["extract-todo", "--match-regex", "hello", str(target)]):
                with redirect_stderr(io.StringIO()):
                    # Must not raise SystemExit(2) (option error) nor re.error.
                    try:
                        main()
                    except SystemExit as e:
                        self.assertNotEqual(e.code, 2)


if __name__ == "__main__":
    unittest.main()
