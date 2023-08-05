"""
Hook implementation for test cases in 'python_demo/pytest' package.
"""
from .test_foo_compare import Foo


def pytest_assertrepr_compare(op, left, right):
    """
    Display string when assert comparing failure.
    :param op:
    :param left:
    :param right:
    :return:
    """
    if isinstance(left, Foo) and isinstance(right, Foo) and op == "==":
        return [
            "Comparing Foo instances:",
            "   vals: {} != {}".format(left.val, right.val),
        ]

    return None
