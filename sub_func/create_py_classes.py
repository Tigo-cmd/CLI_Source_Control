"""this module handles creation of python files especially for up and coming alx students>>>
    creates files append function if needed

####################################################################################################################
Copyright (c) 2024 Emmanuel Tigo, All Rights Reserved
Originally By Nwali Ugonna Emmanuel (Emmanuel Tigo)
###################################################################################################################
    """
import os
import re
from sub_func.create_func_files import is_exists


def create_parent_class(filename="", instance_prototype=""):
    pattern = r'[\w/]+\.py'
    match = re.search(pattern, filename)
    if match:
        class_file = match.group(0)
    """handles class creation and constructor(instance) creation it utilizes regular expression"""
    content = ["#!/usr/bin/python3\n", '"""module documentation"""\n\n',f"class {class_file[:-3]}()\n"
                                                                        f"\t"]
    is_exists(filename, content)