"""
https://doc.pytest.org/en/latest/how-to/mark.html

By using the pytest.mark helper you can easily set metadata on your test functions.
You can find the full list of builtin markers in the API Reference.
Or you can list all the markers, including builtin and custom, using the CLI - pytest --markers.
Here are some of the builtin markers:

usefixtures - use fixtures on a test function or class

filterwarnings - filter certain warnings of a test function

skip - always skip a test function

skipif - skip a test function if a certain condition is met

xfail - produce an “expected failure” outcome if a certain condition is met

parametrize - perform multiple calls to the same test function.

It’s easy to create custom markers or to apply markers to whole test classes or modules.
Those markers can be used by plugins, and also are commonly used to select tests on
the command-line with the -m option.

"""
import pytest


class TestMark:
    @pytest.mark.slow
    def test_slow(self):
        print("mark slow test")

    @pytest.mark.serial
    def test_serial(self):
        print("mark serial test")

    def test_no_mark(self):
        print("no mark test")


if __name__ == '__main__':
    pytest.main(['-s', '-m not slow and not serial', "test_marks.py"])