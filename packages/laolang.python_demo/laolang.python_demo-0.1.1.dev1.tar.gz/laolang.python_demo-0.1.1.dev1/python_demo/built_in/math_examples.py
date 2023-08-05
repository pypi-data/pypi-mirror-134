"""
How to use math methods like 'abs' in built-in functions.
"""


def abs_examples():
    """
    Examples for abs method.

    abs(x) 返回一个数的绝对值。 参数可以是整数、浮点数或任何实现了 __abs__() 的对象。 如果参数是一个复数，则返回它的模。
    :return: None
    """
    print('- abs_examples ----------------')
    print(abs(0.01))
    print(abs(-1999))
    print('- abs_examples ----------------')


def pow_examples():
    """
    Examples for pow method.

    pow(base, exp[, mod])
        返回 base 的 exp 次幂；如果 mod 存在，则返回 base 的 exp 次幂对 mod 取余（比 pow(base, exp) % mod 更高效）。
        两参数形式 pow(base, exp) 等价于乘方运算符: base**exp。
    :return:
    """
    print('- pow_examples ----------------------')
    print(pow(2, 4))
    print(2 ** 4)
    print(pow(2, 4, 5))
    print('- pow_examples ----------------------')


def divmod_examples():
    """
    divmod(a, b)
        以两个（非复数）数字为参数，在作整数除法时，返回商和余数。若操作数为混合类型，则适用二进制算术运算符的规则。
        对于整数而言，结果与 (a // b, a % b) 相同。对于浮点数则结果为``(q, a % b)``，其中 q 通常为 math.floor(a / b)，
        但可能比它小 1。在任何情况下，q * b + a % b 都非常接近 a，如果 a % b 非零，则结果符号与 b 相同，
        并且 0 <= abs(a % b) < abs(b)。
    :return:
    """
    print('- divmod_examples ----------------------')
    print(divmod(100, 7))
    print(divmod(62, 41))
    print('- divmod_examples ----------------------')


def bitwise_operations_on_integer_examples():
    """
    按位运算只对整数有意义。 计算按位运算的结果，就相当于使用无穷多个二进制符号位对二的补码执行操作。
    二进制按位运算的优先级全都低于数字运算，但又高于比较运算；一元运算 ~ 具有与其他一元算术运算 (+ and -) 相同的优先级。
    :return:
    """
    print('- bitwise_operations_on_integer_examples ----------------------')
    v_1 = 10
    v_2 = 50
    print(v_1, bin(v_1), v_2, bin(v_2))
    print(v_1 & v_2, bin(v_1 & v_2))  # 按位 与
    print(v_1 | v_2, bin(v_1 | v_2))  # 按位 或
    print(v_1 ^ v_2, bin(v_1 ^ v_2))  # 按位 异或
    print(v_1 << 1)  # 左移 n 位
    print(v_1 >> 1)  # 右移 n 位
    print(~v_1, bin(~v_1))  # 逐位取反
    print('- bitwise_operations_on_integer_examples ----------------------')


if __name__ == '__main__':
    abs_examples()
    pow_examples()
    divmod_examples()
    bitwise_operations_on_integer_examples()
