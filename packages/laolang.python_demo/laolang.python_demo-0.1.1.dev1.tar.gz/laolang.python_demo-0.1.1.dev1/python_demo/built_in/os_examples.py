"""
Demonstrate how to use the os module.
"""
import os


def environment_variable_examples():
    """
    Examples about environment variable.
    :return: None
    """
    print('- environment_variable_examples --------------------------')
    print(os.environ)

    os.environ['ABC'] = 'C:\\ABC'

    print(os.getenv('ABC'))

    print(os.environ)

    os.putenv('HELLO', 'C:\\Hello')  # change not change os.environ for putenv

    print(os.getenv('ABC'))

    print(os.environ)

    print('- environment_variable_examples --------------------------')


def directory_examples():
    """
    Examples about directory
    :return: None
    """
    print('- directory_examples --------------------------')

    print(os.getcwd())  # current working directory
    os.chdir('../')  # change to up level directory
    print(os.getcwd())  # current working directory

    # Scan current working directory
    for sub_dir in os.scandir(os.getcwd()):
        print(sub_dir)

    print('- directory_examples --------------------------')


def path_examples():
    """
    Examples for path.
    :return: None
    """
    print('- path_examples --------------------------')
    file_path = os.path.realpath(__file__)
    print(file_path)
    dir_path = os.path.dirname(file_path)
    print(dir_path)
    print(os.path.isdir(dir_path))
    print(os.path.isfile(dir_path))
    print(os.path.isdir(file_path))
    print(os.path.isfile(file_path))
    print(os.path.isabs(file_path))
    print(os.path.exists(file_path))
    # basename 将 path 传入函数 split() 之后，返回的一对值中的第二个元素
    print(os.path.basename(file_path))
    print(os.path.basename(dir_path))

    # relative path
    file_name = os.path.relpath(file_path, dir_path)
    print(file_name)
    # absolute path for file name
    os.path.abspath(file_name)

    # split file name and directory
    print(os.path.split(file_path))

    # join file name and directory
    print(os.path.join(dir_path, 'new_file1.txt'))

    print(os.path.splitext(file_path))  # split by extension
    print(os.path.splitdrive(file_path))  # split by drive disk

    print(os.path.getatime(file_path))  # last access time for file
    print(os.path.getctime(file_path))  # create time for file
    print(os.path.getmtime(file_path))  # last modified time for file
    print(os.path.getsize(file_path))  # byte size

    # separator for path
    print(os.path.sep)

    # walk through sub directory and file name
    for root, dirs, files in os.walk(os.getcwd()):
        print(root)
        print(dirs)
        print(files)

    # common prefix or path for multiple paths
    print(os.path.commonprefix(['/usr/lib', '/usr/local/lib']))
    print(os.path.commonpath(['/usr/lib', '/usr/local/lib']))

    print(os.path.expanduser('~sliang'))

    os.environ['ROOT_JAVA'] = 'C:\\Java'
    print(os.path.expandvars('%ROOT_JAVA%\\bin'))

    print('- path_examples --------------------------')


if __name__ == '__main__':
    environment_variable_examples()
    directory_examples()
    path_examples()
