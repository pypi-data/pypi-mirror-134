from setuptools import setup, find_packages

from pj_build.text_version import get_version
setup(
    name="laolang.python_demo",
    version=get_version('./pj_build/version.txt'),
    author="Laolang",
    author_email="laolanglife@163.com",
    description="Learn to use the python 3 and popular open source",

    url="https://github.com/liangshenwen/python_demo.git",
    python_requires='>=3.7, <=3.10',

    packages=find_packages()
)
