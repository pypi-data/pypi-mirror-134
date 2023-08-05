"""
Demonstrate how to use glob module.

https://docs.python.org/zh-cn/3.10/library/glob.html?highlight=glob#module-glob
https://docs.python.org/zh-cn/3.10/library/fnmatch.html#fnmatch.fnmatch
"""
from glob import glob
import os
import fnmatch
import re


def glob_examples():
    print('- glob_examples ---------------------')
    os.chdir('../')
    print(os.getcwd())
    for match in glob(os.path.join(os.getcwd(), '**/*.py'), recursive=True):
        print(match)
    print('- glob_examples ---------------------')


def fnmatch_examples():
    print('- fnmatch_examples ---------------------')
    for file in os.listdir(os.path.dirname(os.path.realpath(__file__))):
        if fnmatch.fnmatch(file, '*.txt'):
            print(file)

    regex = fnmatch.translate('*.txt')  # translate glob style to regular expression.
    print(regex)
    re_obj = re.compile(regex)
    print(re_obj.match('foobar.txt'))
    print('- fnmatch_examples ---------------------')


if __name__ == '__main__':
    glob_examples()
    fnmatch_examples()
