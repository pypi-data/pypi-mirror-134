# Pylint
Home page: https://www.pylint.org/  
Docs: https://pylint.pycqa.org/en/latest/
## Install
Go into the folder of python interpreter and open the command windows, then execute command:
```
python -m pip install pylint
```
## Code Style Guide
https://www.python.org/dev/peps/pep-0008/

## Integrate with Pycharm
https://pylint.pycqa.org/en/latest/user_guide/ide-integration.html#pylint-in-pycharm

## pyenchant for Spelling Check
```
python -m pip install pyenchant
```

# Test
## Pytest
Unit test and integration test tool.  
https://doc.pytest.org/en/latest/index.html  

## Pytest-cov
Pytest plugin for measuring coverage.  

```
python -m pip install pytest-cov
```

Docs: https://pytest-cov.readthedocs.io/en/latest/readme.html
## Pytest-html
pytest-html is a plugin for pytest that generates a HTML report for test results.  

```
python -m pip install pytest-html
```

Docs: https://pytest-html.readthedocs.io/en/latest/  
## Coverage
Coverage.py measures code coverage, typically during test execution. 
It uses the code analysis tools and tracing hooks provided in the Python standard library to 
determine which lines are executable, and which have been executed.

https://github.com/nedbat/coveragepy  

Docs:  
https://coverage.readthedocs.io/en/6.2/#quick-start  
https://coverage.readthedocs.io/en/6.2/index.html#  

## Allure (Generate Unit Test Report)
https://docs.qameta.io/allure/   

Allure Report is a flexible, lightweight multi-language test reporting tool. 
It provides clear graphical reports and allows everyone involved in the development process 
to extract the maximum of information from the everyday testing process.  

https://docs.qameta.io/allure-report/frameworks/python/pytest  

**Download Allure2**   
https://github.com/allure-framework/allure2/releases   
Unzip and add ```ALLURE_HOME``` in environment variable:
{unzip folder}\allure-2.17.2
Add ```%ALLURE_HOME%\bin``` to ```Path``` in environment variable.

**Install allure-pytest**   
```
pip install allure-pytest
```
**Generate allure result**  
```
pytest --alluredir=./allure-result .
```
**Generate allure report**  
```
allure generate -c  ./allure-result -o ./allure-report
```
**Open allure report**  
```
allure open ./allure-report
```
# Documentation
This project uses the sphinx module to produce its documentation.

https://pythonhosted.org/an_example_pypi_project/sphinx.html

First we need to take the docstrings from within the python code and produce .rst files, then generate HTML:
```
sphinx-apidoc -f -o build/source src && cp doc/source/index.rst build/source
sphinx-build -b html -c doc/source build/source/ build/docs/ -a
```

The documents can also generate with setuptools:
```
python setup.py build_sphinx
```

# Poetry
Poetry comes with all the tools you might need to manage your projects in a deterministic way.  
Home page: https://python-poetry.org/