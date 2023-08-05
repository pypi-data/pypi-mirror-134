"""
Demonstrate how to use dict.

https://docs.python.org/zh-cn/3.10/library/stdtypes.html#dict
"""


def dict_example_1():
    """
    字典构造函数
    :return:
    """
    print('-- dict_example_1 -------------------')
    a = dict(one=1, two=2, three=3)
    b = {'one': 1, 'two': 2, 'three': 3}
    c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    d = dict([('two', 2), ('one', 1), ('three', 3)])
    e = dict({'three': 3, 'one': 1, 'two': 2})
    f = dict({'one': 1, 'three': 3}, two=2)
    print(a == b == c == d == e == f)
    print('-- dict_example_1 -------------------')


def dict_example_2():
    """
    字典推导式:
    对于字典，它和列表、元组一样，也可以使用字典推导式来快速的生成一个字典，它的表现形式和列表推导式类似，只不过将列表推导式中的中括号[]改为大括号{}：
    {键表达式：值表达式 for 循环}
    :return:
    """
    print('-- dict_example_2 -------------------')
    numbers = [1, 2, 3]
    d_1 = dict([(number, number * 2) for number in numbers])
    print(d_1)

    d_2 = {x: x * 2 for x in numbers}
    print(d_2)
    print(d_1 == d_2)

    name = ['Allen', 'Bird', 'Jason']
    sex = ['F', 'M', 'F']
    d_3 = {i:j for i, j in zip(name, sex)}
    print(d_3)
    print('-- dict_example_2 -------------------')


def dict_example_3():
    """
    d[key]
       返回 d 中以 key 为键的项。 如果映射中不存在 key 则会引发 KeyError。

       如果字典的子类定义了方法 __missing__() 并且 key 不存在，则 d[key] 操作将调用该方法并附带键 key 作为参数。
       d[key] 随后将返回或引发 __missing__(key) 调用所返回或引发的任何对象或异常。
       没有其他操作或方法会发起调用 __missing__()。 如果未定义 __missing__()，则会引发 KeyError。
       __missing__() 必须是一个方法；它不能是一个实例变量:
    :return:
    """
    print('-- dict_example_3 -------------------')

    class Counter(dict):
        def __missing__(self, key):
            return 0

    c = Counter()
    print(c['red'])
    c['red'] += 1
    print(c['red'])
    print('-- dict_example_3 -------------------')


if __name__ == '__main__':
    dict_example_1()
    dict_example_2()
    dict_example_3()
