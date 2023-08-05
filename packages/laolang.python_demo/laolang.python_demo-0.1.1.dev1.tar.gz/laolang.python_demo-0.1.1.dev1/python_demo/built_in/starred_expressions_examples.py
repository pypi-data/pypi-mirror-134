"""
Demonstrate how to use * and ** in python 3.
"""


def star_example_1():
    """
    加了星号（*）的变量名会存放所有未命名的变量参数，不能存放dict，否则报错。
    :return:
    """
    print('-- star_example_1 -----------------')

    def multiple(arg, *args):
        print("arg: ", arg)
        # 打印不定长参数
        for value in args:
            print("other args:", value)

    multiple(1, 'a', True)
    print('-- star_example_1 -----------------')


def star_example_2():
    """
    加了星号（**）的变量名会存放所有未命名的变量参数
    :return:
    """
    print('-- star_example_2 -----------------')

    def multiple(arg, *args, **kwargs):
        print("arg: ", arg)
        # 打印不定长参数
        for value in args:
            print("other args:", value)
        # 打印dict类型的不定长参数 args
        for key in kwargs:
            print(key, "=", kwargs[key])

    multiple(1, 3, 4, a='a', b=True)
    print('-- star_example_2 -----------------')


def star_example_3():
    """
    在Python数学运算中*代表乘法，**为指数运算
    :return:
    """
    print('-- star_example_3 -----------------')
    print(2 * 3)
    print(2 ** 3)
    print('-- star_example_3 -----------------')


def star_example_4():
    """
    如果函数的形参是定长参数，也可以使用 *args 和 **kwargs 调用函数，类似对元组和字典进行解引用：
    :return:
    """
    print('-- star_example_4 -----------------')

    def fun(data1, data2, data3):
        print("data1: ", data1)
        print("data2: ", data2)
        print("data3: ", data3)
    args = ("one", 2, 3)

    fun(*args)
    kwargs = {"data3": "one", "data2": 2, "data1": 3}
    fun(**kwargs)

    # * 获取的值默认为 list
    # 获取剩余部分：
    a, b, *c = 0, 1, 2, 3
    print(a)
    print(b)
    print(c)

    # 获取中间部分：
    a, *b, c = 0, 1, 2, 3
    print(a)
    print(b)
    print(c)

    # 如果左值比右值要多，那么带 * 的变量默认为空
    a, b, *c = 0, 1
    print(a)
    print(b)
    print(c)
    a, *b, c = 0, 1
    print(a)
    print(b)
    print(c)
    print('-- star_example_4 -----------------')


if __name__ == '__main__':
    star_example_1()
    star_example_2()
    star_example_3()
    star_example_4()
