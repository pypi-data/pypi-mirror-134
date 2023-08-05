"""
Run the unit tests for all modules in 'pj_build' package
"""
import pytest

if __name__ == '__main__':
    print('run all test cases in <pj_build> folder')
    pytest.main(['-x',
                 '--cov=pj_build',
                 '--cov-report=html',
                 '--html=unit_test_report.html',
                 '.'])
