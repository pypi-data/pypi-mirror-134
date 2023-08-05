"""
Demonstrate Sequence unpacking in python3
"""


def seq_unpack_example_1():
    """
    如果函数的形参是定长参数，也可以使用 *args 和 **kwargs 调用函数，类似对元组和字典进行解引用：
    :return:
    """
    print('-- seq_unpack_example_1 -----------------')

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

    # 嵌套解包
    (a, b), (c, d) = (1, 2), (3, 4)
    print(a, b, c, d)
    l = a, b, c, d
    print(l)
    print('-- seq_unpack_example_1 -----------------')


def seq_unpack_example_2():
    """
    假如一个字符串 'ABCDEFGH'，要输出下列格式:
A ['B', 'C', 'D', 'E', 'F', 'G', 'H']
B ['C', 'D', 'E', 'F', 'G', 'H']
C ['D', 'E', 'F', 'G', 'H']
D ['E', 'F', 'G', 'H']
E ['F', 'G', 'H']
F ['G', 'H']
G ['H']
H []
    :return:
    """
    print('-- seq_unpack_example_2 -----------------')
    # 传统方法
    # 一般的处理过程是:
    # 1. 将切片中索引为 0 的字符赋值给 a
    # 2. 将切片中索引为 1 之后字符再赋值给 s
    # 3. 用 list 函数将字符串转变为列表
    # 4. 用 while 循环来 s 来判断，为空，则退出循环
    s = 'ABCDEFGH'
    while s:
        x, s = s[0], list(s[1:])
        print(x, s)

    # 上面的处理，可以用序列解包的方法会来处理。序列解包，在赋值时无疑更方便、更简洁、更好理解、适用性更强！
    # 运用序列解包的功能重写上面的代码：
    s = 'ABCDEFGH'
    while s:
        x, *s = s
        print(x, s)

    print('-- seq_unpack_example_2 -----------------')


if __name__ == '__main__':
    seq_unpack_example_1()
    seq_unpack_example_2()
