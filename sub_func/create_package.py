"""this modue handles package creation for python"""

import os

def create_package(rootdir="", subdir=""):
    """implements the package creation
    Args:
        rootdir: this is the parent directory or package name
        subdir: sub folders and directory for package
    """
    if rootdir != "":
        # creates the directory
        os.mkdir(rootdir, 0o764)
        #adds the __init__ file...
        init_file = "__init__.py"
        with open(init_file, 'w', encoding='utf-8':