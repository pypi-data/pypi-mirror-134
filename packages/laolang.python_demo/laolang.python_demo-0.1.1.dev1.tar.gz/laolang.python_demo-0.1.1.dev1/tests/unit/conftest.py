"""
Configuration for pytest.
"""


def pytest_report_header(config):
    """
    Generate the report header for project.
    :param config:
    :return: The report header for unit tests
    """
    print('config:', config)
    return 'unit tests for python demo project'
