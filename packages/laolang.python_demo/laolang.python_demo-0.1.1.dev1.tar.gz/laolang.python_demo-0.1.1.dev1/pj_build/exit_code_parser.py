"""
Parse the exit code from different component like pytest, pylint.
"""
import sys


def parse_pylint(exit_code):
    """
    Parse the exit code from pylint.
    :param exit_code:
    :return: If an error or a fatal message was issued, return True, otherwise return False
    """

    b_fail = False

    print('pylint exit code: (', exit_code, format(exit_code, 'b'), ')')
    if exit_code == 0:
        print('pylint: everything went fine')

    if exit_code & 1 == 1:
        print('pylint: a fatal message was issued')
        b_fail = True
    if exit_code & 2 == 2:
        print('pylint: an error message was issued')
        b_fail = True
    if exit_code & 4 == 4:
        print('pylint: a warning message was issued')
    if exit_code & 8 == 8:
        print('pylint: a refactor message was issued')
    if exit_code & 16 == 16:
        print('pylint: a convention message was issued')
    if exit_code & 32 == 32:
        print('pylint: usage error')

    return b_fail


if __name__ == '__main__':
    print('sys.argv:', sys.argv)
    if len(sys.argv) >= 3:
        app_type = sys.argv[1]
        app_exit_code = int(sys.argv[2])
        if app_type == 'pylint':
            if parse_pylint(app_exit_code):
                exit(-1)
            else:
                exit(0)
    else:
        print('Usage: python exit_code_parser.py app_type app_exit_code')
        exit(-1)
