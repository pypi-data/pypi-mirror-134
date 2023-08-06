# See ocdskit/tests/__init__.py
import os.path
import sys
from difflib import ndiff
from io import BytesIO, TextIOWrapper
from itertools import zip_longest
from unittest.mock import patch

import ocdskit.util


def path(filename):
    return os.path.join("tests", "fixtures", filename)


def read(filename, mode="rt", encoding=None, **kwargs):
    with open(path(filename), mode, encoding=encoding, **kwargs) as f:
        return f.read()


def assert_equal(actual, expected, ordered=True):
    if ordered:
        assert actual == expected, "".join(
            ndiff(actual.splitlines(1), expected.splitlines(1))
        )
    else:
        for a, b in zip_longest(
            actual.split("\n"), expected.split("\n"), fillvalue="{}"
        ):
            if a != b != "":
                assert ocdskit.util.jsonlib.loads(a) == ocdskit.util.jsonlib.loads(
                    b
                ), f"\n{a}\n{b}"


def run_streaming(capsys, monkeypatch, main, args, stdin):
    if not isinstance(stdin, bytes):
        stdin = b"".join(read(filename, "rb") for filename in stdin)

    with patch("sys.stdin", TextIOWrapper(BytesIO(stdin))):
        monkeypatch.setattr(sys, "argv", ["ocdskit"] + args)
        main()

    return capsys.readouterr()


def assert_streaming(capsys, monkeypatch, main, args, stdin, expected, ordered=True):
    actual = run_streaming(capsys, monkeypatch, main, args, stdin)

    if not isinstance(expected, str):
        expected = "".join(read(filename) for filename in expected)

    assert_equal(actual.out, expected, ordered=ordered)
