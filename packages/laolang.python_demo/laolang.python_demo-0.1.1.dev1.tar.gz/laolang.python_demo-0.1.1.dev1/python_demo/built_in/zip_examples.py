"""
Demonstrate how to use zip and unzip.

https://docs.python.org/zh-cn/3.10/library/functions.html#zip

zip(*iterables, strict=False)
在多个迭代器上并行迭代，从每个迭代器返回一个数据项组成元组。

    zip() 返回元组的迭代器，其中第 i 个元组包含的是每个参数迭代器的第 i 个元素。

    不妨换一种方式认识 zip() ：它会把行变成列，把列变成行。这类似于 矩阵转置 。

    zip() 是延迟执行的：直至迭代时才会对元素进行处理，比如 for 循环或放入 list 中。
"""
import traceback


def zip_example_1():
    print('-- zip_example_1 ------------')
    for item in zip([1, 2, 3], ['sugar', 'spice', 'everything nice']):
        print(item)
    print('-- zip_example_1 ------------')


def zip_example_2():
    """
    传给 zip() 的可迭代对象可能长度不同；有时是有意为之，有时是因为准备这些对象的代码存在错误。Python 提供了三种不同的处理方案：
    :return:
    """
    print('-- zip_example_2 ------------')
    # strict 参数必须是3.10以上的版本才支持
    # 1) 默认情况下，zip() 在最短的迭代完成后停止。较长可迭代对象中的剩余项将被忽略，结果会裁切至最短可迭代对象的长度：
    print(list(zip(range(3), ['fee', 'fi', 'fo', 'fum'])))
    # 2)通常 zip() 用于可迭代对象等长的情况下。这时建议用 strict=True 的选项。输出与普通的 zip() 相同：。
    # 与默认行为不同的是，它会检查可迭代对象的长度是否相同，如果不相同则触发 ValueError 。
    # 如果未指定 strict=True 参数，所有导致可迭代对象长度不同的错误都会被抑制，这可能会在程序的其他地方表现为难以发现的错误。
    try:
        print(list(zip(('a', 'b', 'c'), (1, 2, 3), strict=True)))
    except Exception as e:
        traceback.print_exc()

    try:
        list(zip(range(3), ['fee', 'fi', 'fo', 'fum'], strict=True))
    except Exception as e:
        traceback.print_exc()
    # 为了让所有的可迭代对象具有相同的长度，长度较短的可用常量进行填充。这可由 itertools.zip_longest() 来完成。
    import itertools
    try:
        print(list(itertools.zip_longest(range(3), ['fee', 'fi', 'fo', 'fum'], fillvalue=-1)))
    except Exception as e:
        traceback.print_exc()

    print('-- zip_example_2 ------------')


def zip_example_3():
    print('-- zip_example_3 ------------')
    x = [1, 2, 3]
    y = [4, 5, 6]
    zipped = zip(x, y)
    print(list(zipped))
    x2, y2 = zip(*zip(x, y))
    print(x == list(x2) and y == list(y2))
    print('-- zip_example_3 ------------')


if __name__ == '__main__':
    zip_example_1()
    zip_example_2()
    zip_example_3()
