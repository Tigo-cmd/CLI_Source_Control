"""this module handles creation of python files especially for up and coming alx students>>>
    creates files append function if needed

####################################################################################################################
Copyright (c) 2024 Emmanuel Tigo, All Rights Reserved
Originally By Nwali Ugonna Emmanuel (Emmanuel Tigo)
###################################################################################################################
    """
import os


def create_parent_class(filename="", instance_prototype=""):
    """handles class creation and constructor(instance) creation"""
    content = ["#!/usr/bin/python3\n", '"""module documentation"""\n\n',f"class {filename[:-3]}()\n"
                                                                        f"\t{instance_prototype}"
                                                                        f"\n\t", "if __name__ == '__main__':"]
    if os.path.exists(filename):
        """checks if file exists in the current directory and overwrites when prompted"""
        overwrite = input(f"{filename} already exists Overwrite?(Y/N): ").lower()
        if 'y' in overwrite:
            instance_prototype = input(f"instance_prototype for {filename}: ")
            with open(filename, 'w', encoding='utf-8') as f:
                # creates file and writes contents to each line of the file
                f.writelines(content)
            os.chmod(filename, 0o764)
        elif 'n' in overwrite:
            pass
        else:
            print("invalid input")
            pass
    else:  # checks if the prototype was given else asks user to input
        instance_prototype = input(f"prototype for {filename}: ")  # prototype is stored in the variable
        with open(filename, 'w', encoding='utf-8') as f:
            # creates file and writes contents to each line of the file
            f.writelines(content)
        os.chmod(filename, 0o764)  # set the file permission of the file to executable
