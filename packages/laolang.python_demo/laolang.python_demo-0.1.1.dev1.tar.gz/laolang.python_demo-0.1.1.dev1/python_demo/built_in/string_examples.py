"""
Demonstrate how to use string module.

https://docs.python.org/zh-cn/3.10/library/string.html

"""
import string
from string import Template


def special_prefix_examples():
    print('- special_prefix_examples ---------------')
    # r'' 去掉反斜杠的转义机制。
    #
    # （特殊字符：即那些，反斜杠加上对应字母，表示对应的特殊含义的，比如最常见的”\n”表示换行，”\t”表示Tab等。 ）
    #
    # 应用：
    #
    # 常用于正则表达式，对应着re模块。
    s_1 = r'\n\r'
    print(s_1)

    # b'' 前缀表示：后面字符串是bytes 类型。
    #
    # 用处：
    #
    # 网络编程中，服务器和浏览器只认bytes 类型数据。
    #
    # 如：send 函数的参数和 recv 函数的返回值都是 bytes 类型
    # 附：
    #
    # 在 Python3 中，bytes 和 str 的互相转换方式是
    # str.encode('utf-8')
    # bytes.decode('utf-8')
    response = b'<h1>Hello World!</h1>'  # b' ' 表示这是一个 bytes 对象
    print(response)

    # u"我是含有中文字符组成的字符串。"
    #
    # 作用：
    #
    # 后面字符串以 Unicode 格式 进行编码，一般用在中文字符串前面，防止因为源码储存格式问题，导致再次使用时出现乱码。
    name = u'老实人'
    print(name)

    # f-string(https://docs.python.org/3/library/string.html#format-string-syntax)
    # 格式化 {} 内容，不在 {} 内的照常展示输出，如果你想输出 {}，那就用双层 {undefined{}} 将想输出的内容包起来。
    str_l = ['a', 'b']
    print(str_l, f' has length of {len(str_l)}')
    print(str_l, f' has length of {{len(str_l)}}')
    print(str_l, f' has length of {{{len(str_l)}}}')
    print(str_l, ' has length of {len(str_l)}')
    print('- special_prefix_examples ---------------')


def capwords_examples():
    print('- capwords_examples ---------------')
    # 使用 str.split() 将参数拆分为单词，使用 str.capitalize() 将单词转为大写形式，使用 str.join() 将大写的单词进行拼接。
    print(string.capwords('hello world', ' '))
    print(string.capwords('HellO world', ' '))
    print('- capwords_examples ---------------')


def template_examples():
    print('- template_examples ---------------')
    s = Template('$who likes $what')
    print(s.substitute(who='tim', what='kung pao'))

    d = dict(who='tim')
    try:
        print(Template('$who likes $what').substitute(d))
    except KeyError as e:
        print(e)

    print(Template('$who likes $what').safe_substitute(d))
    print('- template_examples ---------------')


def format_examples():
    print('- format_examples ---------------')
    print('{0}, {1}, {2}'.format('a', 'b', 'c'))
    print('{}, {}, {}'.format('a', 'b', 'c'))  # 3.1+ only)
    print('{2}, {1}, {0}'.format('a', 'b', 'c'))
    print('{2}, {1}, {0}'.format(*'abc'))      # unpacking argument sequence
    print('{0}{1}{0}'.format('abra', 'cad'))   # arguments' indices can be repeated
    print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W'))
    coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
    print('Coordinates: {latitude}, {longitude}'.format(**coord))  # unpacking dictionary
    c = 3 - 5j
    print('The complex number {0} is formed from the real part {0.real} and the imaginary part {0.imag}.'
          .format(c))

    class Point:
        def __init__(self, x, y):
            self.x, self.y = x, y

        def __str__(self):
            return 'Point({self.x}, {self.y})'.format(self=self)

    print(str(Point(4, 2)))
    coord = (3, 5)
    print('X: {0[0]};  Y: {0[1]}'.format(coord))  # 访问参数的项
    print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))  # 替代 %s 和 %r:

    # 对齐文本以及指定宽度
    print('{:<30}'.format('left aligned'))
    print('{:>30}'.format('right aligned'))
    print('{:^30}'.format('centered'))
    print('{:*^30}'.format('centered'))  # use '*' as a fill char)

    # 替代 %+f, %-f 和 % f 以及指定正负号
    print('{:+f}; {:+f}'.format(3.14, -3.14))  # show it always
    print('{: f}; {: f}'.format(3.14, -3.14))  # show a space for positive numbers
    print('{:-f}; {:-f}'.format(3.14, -3.14))  # show only the minus -- same as '{:f}; {:f}'

    # 替代 %x 和 %o 以及转换基于不同进位制的值
    # format also supports binary numbers
    print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))

    # with 0x, 0o, or 0b as prefix:
    print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42))
    print('{:,}'.format(1234567890))  # 使用逗号作为千位分隔符

    points = 19
    total = 22
    print('Correct answers: {:.2%}'.format(points / total))  # 表示为百分数

    for align, text in zip('<^>', ['left', 'center', 'right']):
        print('{0:{fill}{align}16}'.format(text, fill=align, align=align))

    octets = [192, 168, 0, 1]
    print('{:02X}{:02X}{:02X}{:02X}'.format(*octets))

    width = 5
    for num in range(5, 12):
        for base in 'dXob':
            print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
        print()

    print('- format_examples ---------------')


if __name__ == '__main__':
    special_prefix_examples()
    capwords_examples()
    template_examples()
    format_examples()
