import os


def expand_path(path, *paths):
    return os.path.join('test', 'test_balsam', 'fixtures', path, *paths)
