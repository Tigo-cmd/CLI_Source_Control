"""this module handles package creation for python"""

import os


def create_package(dir=""):
    """implements the package creation
    Args:
        dir: this is the parent directory or package name
    """
    if dir != "":
        # creates the directory
        os.mkdir(dir, 0o764)
        # changes dir to dir and creates the init.py file
        os.chdir(dir)
        # adds the __init__ file...
        init_file = "__init__.py"
        with open(init_file, 'w', encoding='utf-8') as f:
            pass
    else:
        pass
