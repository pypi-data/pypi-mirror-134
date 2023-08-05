"""
Run unit tests for all modules in 'python_demo/pytest' package.
"""
import os
from glob import glob
import pytest

if __name__ == '__main__':
    cur_path = os.path.realpath(__file__)
    dir_path = os.path.dirname(cur_path)
    results = []
    for root, dirs, files in os.walk(dir_path):
        for match in glob(os.path.join(root, 'test_*.py')):
            results.append(match)
    print('run all test cases in <python_demo/pytest> folder')
    print('test modules:', results)
    pytest.main([''])
