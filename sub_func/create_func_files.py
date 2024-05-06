"""this module handles creation of python files for alx students>>>
    creates files append function if needed"""
import os
# import subprocess


def source_code_create(filename="", prototype=""):
    """handles creating python functions files
     and setting necessary permissions
        Args:
            filename: name of file to be created, must be a python file extension
            prototype: this is the alx provided function eg: def create_file(filename=""):
            """
    if os.path.exists(filename):
        """checks if file exists in the current directory and overwrites when prompted"""
        overwrite = input(f"{filename} already exists Overwrite?(Y/N): ").lower()
        if 'y' in overwrite:
            prototype = input(f"prototype for {filename}: ")
            content = ["#!/usr/bin/python3\n", '"""module documentation"""\n\n', f"{prototype}\n"]
            with open(filename, 'w', encoding='utf-8') as f:
                # creates file and writes contents to each line of the file
                f.writelines(content)
            os.chmod(filename, 0o764)
        elif 'n' in overwrite:
            pass
        else:
            print("invalid input")
            pass
    elif filename[-3:] != '.py':  # checks if the file is a python file
        with open(filename, 'w', encoding='utf-8') as file:
            pass
        print("created an empty file")
    elif prototype == "":  # checks if the prototype was given else asks user to input
        prototype = input(f"prototype for {filename}: ")  # prototype is stored in the variable
    content = ["#!/usr/bin/python3\n", '"""module documentation"""\n\n', f"{prototype}\n"]
    with open(filename, 'w', encoding='utf-8') as f:
        # creates file and writes contents to each line of the file
        f.writelines(content)
    os.chmod(filename, 0o764)  # set the file permission of the file to executable


def file_create(filename=""):
    """creates normal python file users adds codes to taste
        Args:
            filename: file to be creates by function
            if file extension is invalid the program will yell out
            """
    if filename[-3:] == '.py':
        content = ["#!/usr/bin/python3\n", '"""module documentation"""\n\n', "if __name__ == '__main__':"
                                                                             "    "]
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(content)
        os.chmod(filename, 0o764)
    elif os.path.exists(filename):
        overwrite = input(f"{filename} already exists Overwrite?(Y/N): ").lower()
        if 'y' in overwrite:
            with open(filename, 'w', encoding='utf-8') as file:
                pass
        elif 'n' in overwrite:
            pass
        else:
            print("invalid input")
            pass
    else:
        with open(filename, 'w', encoding='utf-8') as file:
            pass
        print("created an empty file")


def test_prototype(filename=""):
    """this creates a test file prototype with common startup lines"""
    content = ["#!/usr/bin/python3\n", '"""module documentation"""',
               "import unittest\n\n", f"class Test_{filename}(unittest.Testcase):"
                                      f"    def setup():\n", "if __name__ == '__main__':"
                                      "    unittest.main()"]
    if "test" in filename:
        if os.path.exists(filename):
            overwrite = input(f"{filename} already exists Overwrite?(Y/N): ").lower()
            if 'y' in overwrite:
                with open(filename, 'w', encoding='utf-8') as file:
                    file.writelines(content)
                os.chmod(filename, 0o764)
            elif 'n' in overwrite:
                pass
            else:
                print("invalid input")
                pass
        with open(filename, 'w', encoding='utf-8') as file:
            file.writelines(content)
        os.chmod(filename, 0o764)
