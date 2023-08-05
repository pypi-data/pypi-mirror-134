"""
Replace the project version by git tag.
"""
import sys
import toml
from pj_build.text_version import verify_git_version


def modify_project_toml(git_tag, config_file):
    """
    Use the git tag to update the version pyproject.toml for poetry project.

    :param git_tag: The git tag from git repository.
    :param config_file: The file path for pyproject.toml of poetry project.
    :return: None
    """
    git_tag = verify_git_version(git_tag)

    config_dict = toml.load(config_file)
    print('old pyproject.toml:\n', config_dict)
    config_dict['tool']['poetry']['version'] = git_tag
    with open(config_file, mode='w', encoding='UTF-8') as cfg_f:
        toml.dump(config_dict, cfg_f)

    print('new pyproject.toml:\n', config_dict)


if __name__ == '__main__':
    print('sys.argv:', sys.argv)

    origin_git_tag: str = ''
    if len(sys.argv) > 1:
        origin_git_tag = sys.argv[1]
    else:
        raise Exception('Please input the git tag like 0.1.1 or 0.1.1.dev1')

    modify_project_toml(origin_git_tag, '../pyproject.toml')
