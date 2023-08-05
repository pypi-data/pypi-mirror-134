"""
Demonstrate how to use the attribute methods.
"""


class Abc:
    """
    Just for test
    """
    pass


def attr_example_1():
    print('-- attr_example_1 -------------------')
    abc = Abc()
    setattr(abc, 'name', 'abc1')
    setattr(abc, 'sex', 'male')
    print(dir(abc))

    print(hasattr(abc, 'name'))
    print(hasattr(abc, 'sex'))
    print(getattr(abc, 'name'))
    print(abc.sex)
    delattr(abc, 'name')
    del abc.sex

    print(hasattr(abc, 'name'))
    print(hasattr(abc, 'sex'))

    print(dir(abc))
    print('-- attr_example_1 -------------------')

if __name__ == '__main__':
    attr_example_1()
