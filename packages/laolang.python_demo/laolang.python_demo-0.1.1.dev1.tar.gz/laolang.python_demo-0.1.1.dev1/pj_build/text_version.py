"""
Generate version.txt from git tag.
"""
import re
import sys


def verify_git_version(git_tag):
    if git_tag.startswith('origin/'):
        git_tag = git_tag.replace('origin/', '')

    git_tag = git_tag.strip()
    if len(git_tag.strip()) <= 0:
        raise Exception('git tag can not be blank.')

    match_obj = re.match(r'^\d+.\d+.\d+(.dev\d*)?$', git_tag)
    if not match_obj:
        raise Exception(r'git tag can not match specific format. For release: \d.\d.\d like 0.1.1. '
                        r'For development: \d.\d.\d.dev.\d like 0.1.1.dev1')

    return git_tag


def write_version(git_tag, path='version.txt'):
    with open(path, mode='w') as f:
        f.write(git_tag)

    print('write git tag ', git_tag, 'to version.txt')


def get_version(path='version.txt'):
    with open(path, mode='r') as f:
        version = f.read()
        verify_git_version(version)
        print('get version ', version, 'from version.txt')
        return version


if __name__ == '__main__':
    print('sys.argv:', sys.argv)

    origin_git_tag: str = ''
    if len(sys.argv) > 1:
        origin_git_tag = sys.argv[1]
    else:
        raise Exception('Please input the git tag like 0.1.1 or 0.1.1.dev1')

    git_tag = verify_git_version(origin_git_tag)

    write_version(git_tag)

    print(get_version())



