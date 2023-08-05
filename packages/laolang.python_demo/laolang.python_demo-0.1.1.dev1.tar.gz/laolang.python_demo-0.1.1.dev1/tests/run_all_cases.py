"""
Run all test cases in 'tests' folder.
"""
import os

import pytest

if __name__ == '__main__':
    print('run all test cases in including unit test and integration test')
    pytest.main(['-x',
                 '--cov=python_demo',
                 '--cov=pj_build',
                 '--cov=pj_deploy',
                 '--cov-report=html',
                 '--cov-report=xml',
                 '--html=unit_test_report.html',
                 '--alluredir=./allure-result',
                 '.'])
    current_dir = os.path.dirname(os.path.realpath(__file__))
    print('current dir:', current_dir)
    allure_result_dir = os.path.join(current_dir, 'allure-result')
    allure_report_dir = os.path.join(current_dir, 'allure-report')
    if "ALLURE_HOME" in os.environ:
        allure_home = os.environ["ALLURE_HOME"]
        allure_bat = os.path.join(allure_home, 'bin' + os.path.sep + 'allure.bat')
        print(allure_home)
        print(allure_bat)
        allure_gen_cmd = 'cmd.exe /c ' + allure_bat + ' generate -c -o "' + allure_report_dir \
                         + '" "' + allure_result_dir + '"'
        print(allure_gen_cmd)
        allure_open_cmd = 'cmd.exe /c ' + allure_bat + ' open "' + allure_report_dir + '"'
        print(allure_open_cmd)
        proc_gen = os.popen(allure_gen_cmd)
        proc_gen.close()
        proc_open = os.popen(allure_open_cmd)
        proc_open.close()
    else:
        print('please add ALLURE_HOME to System Environment Variables')
