# -*- encoding: utf-8 -*-
"""
@Author  : zh_o
"""
import os
from typing import Text


def __locate_file(start_path: Text, file_name: Text) -> Text:
    """ locate filename and return absolute file path.
        searching will be recursive upward until system root dir.

    Args:
        file_name (str): target locate file name
        start_path (str): start locating path, maybe file path or directory path

    Returns:
        str: located file path. None if file not found.

    Raises:
        exceptions.FileNotFound: If failed to locate file.

    """
    if os.path.isfile(start_path):
        start_dir_path = os.path.dirname(start_path)
    elif os.path.isdir(start_path):
        start_dir_path = start_path
    else:
        raise Exception(f"invalid path: {start_path}")

    file_path = os.path.join(start_dir_path, file_name)
    if os.path.isfile(file_path):
        # ensure absolute
        return os.path.abspath(file_path)

    # system root dir
    # Windows, e.g. 'E:\\'
    # Linux/Darwin, '/'
    parent_dir = os.path.dirname(start_dir_path)
    if parent_dir == start_dir_path:
        raise Exception(f"{file_name} not found in {start_path}")

    # locate recursive upward
    return __locate_file(parent_dir, file_name)


CONFIG_PATH = os.path.join('./', 'melon.toml')
ROOT_DIR = os.path.abspath(CONFIG_PATH)
