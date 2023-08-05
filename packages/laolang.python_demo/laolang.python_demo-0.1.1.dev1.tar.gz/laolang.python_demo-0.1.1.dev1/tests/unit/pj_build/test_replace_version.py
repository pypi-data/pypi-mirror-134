"""
Unit test for replace_version.py.
"""
from os import path
import shutil
import pytest
import toml
from pj_build import replace_version


def get_test_file(file_name):
    """
    Get the real path for test file related to test_*.py.

    :param file_name: The name for test file in relative folder.
    :return: The real path for test file.
    """
    cur_path = path.realpath(__file__)
    dir_path = path.dirname(cur_path)
    return path.join(dir_path, file_name)


def test_modify_project_toml__git_tag_is_blank():
    """
    Test case: If the git tag is blank, an exception will be raised.

    :return: None
    """
    origin_config_file = get_test_file('pyproject_test.toml')
    test_config_file = origin_config_file + '.1'
    test_config_file = shutil.copyfile(origin_config_file, test_config_file)
    exception_msg = 'git tag can not be blank.'
    with pytest.raises(Exception, match=exception_msg):
        replace_version.modify_project_toml('', test_config_file)

    with pytest.raises(Exception, match=exception_msg):
        replace_version.modify_project_toml('  ', test_config_file)


def test_modify_project_toml__git_tag_is_not_meet_format():
    """
    Test Case: If the git tag doesn't meet the expected format, an exception will be raised.

    :return: None
    """
    origin_config_file = get_test_file('pyproject_test.toml')
    test_config_file = origin_config_file + '.2'
    test_config_file = shutil.copyfile(origin_config_file, test_config_file)
    exception_msg = 'git tag can not match specific format.'
    with pytest.raises(Exception, match=exception_msg):
        replace_version.modify_project_toml('a.b.c', test_config_file)

    with pytest.raises(Exception, match=exception_msg):
        replace_version.modify_project_toml('1.1d.2', test_config_file)


def test_modify_project_toml__git_tag_is_release_version():
    """
    Test Case: If the git tag is for release, update the project version by git tag.

    :return: None
    """
    origin_config_file = get_test_file('pyproject_test.toml')
    test_config_file = origin_config_file + '.3'
    test_config_file = shutil.copyfile(origin_config_file, test_config_file)
    git_tag = '1.1.1000'

    replace_version.modify_project_toml(git_tag, test_config_file)

    config_dict = toml.load(test_config_file)
    assert config_dict['tool']['poetry']['version'] == git_tag


def test_modify_project_toml__git_tag_is_dev_version():
    """
    Test Case: If the git tag is for development, update the project version by git tag.

    :return: None
    """
    origin_config_file = get_test_file('pyproject_test.toml')
    test_config_file = origin_config_file + '.4'
    test_config_file = shutil.copyfile(origin_config_file, test_config_file)
    git_tag = '1.1.1000.dev1'

    replace_version.modify_project_toml(git_tag, test_config_file)

    config_dict = toml.load(test_config_file)
    assert config_dict['tool']['poetry']['version'] == git_tag


if __name__ == '__main__':
    pytest.main(['test_replace_version.py'])
