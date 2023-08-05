"""
https://doc.pytest.org/en/latest/how-to/assert.html

Defining your own explanation for failed assertions.
It is possible to add your own detailed explanations by implementing the pytest_assertrepr_compare hook.

pytest_assertrepr_compare(config, op, left, right)[source]
Return explanation for comparisons in failing assert expressions.

Return None for no custom explanation, otherwise return a list of strings.
The strings will be joined by newlines but any newlines in a string will be escaped.
Note that all but the first line will be indented slightly, the intention is for the first line to be a summary.

Parameters
config (pytest.Config) – The pytest config object.

op (str) –

left (object) –

right (object) –

Return type
Optional[List[str]]

"""

import pytest


class Foo:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

    def get_val(self):
        return self.val


def test_compare():
    f1 = Foo(1)
    f2 = Foo(2)
    assert f1 == f2


if __name__ == "__main__":
    pytest.main(['test_foo_compare.py'])
