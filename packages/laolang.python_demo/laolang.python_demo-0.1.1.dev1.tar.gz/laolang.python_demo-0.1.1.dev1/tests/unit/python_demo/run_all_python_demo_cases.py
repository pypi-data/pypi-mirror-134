"""
Run unit tests for all modules in 'python_demo' package.
"""
import pytest

if __name__ == '__main__':
    print('run all test cases in <python_demo> folder')
    pytest.main(['-x',
                 '--cov=python_demo',
                 '--cov-report=html',
                 '--html=unit_test_report.html',
                 '.'])
