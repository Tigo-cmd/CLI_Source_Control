#!/usr/bin/python3
"""sc source_control main file
a simple git automation script to git your hands of stressful commit and stages
####################################################################################################################
Copyright (c) 2024 Emmanuel Tigo, All Rights Reserved
Originally By Nwali Ugonna Emmanuel (Emmanuel Tigo)
###################################################################################################################
"""

from sub_func.repo import Git
from sub_func.create_py_classes import create_parent_class
from sub_func.create_package import create_package
from sub_func.create_func_files import source_code_create, file_create
from argparse import ArgumentParser, Namespace
import sys
import os

main_entr = Git()


#  main entry of the code, runs all functionalities
def main():
    """main function calls all necessary functions for functionality"""
    """Handles the command line interface interaction utilizing the Argparse module"""
    source = ArgumentParser(description="Command Line Source Control", prog="SC")
    source.add_argument('-d', '--mkpkg', metavar="package_dir", nargs='+', help="creates packages with init files")
    source.add_argument('-t', '--touch', metavar="filename", nargs='+', help="creates files")
    source.add_argument('-t+', '--function', metavar="filename", nargs='+', help="creates files")
    source.add_argument('-t++', '--class_create', metavar="filename", nargs='+', help="creates files")
    source.add_argument('-a', '--add', metavar='', nargs='+', help="add changes to the git")
    source.add_argument('-c', '--commit', metavar='', nargs='?', help="commits changes to the git",
                        const="New Commit")
    source.add_argument('-p', '--push', metavar='', help="Update remote refs along with associated objects",
                        action="store_const", const="pushed")
    source.add_argument('--version', action='version', version="SC 1.0")
    source_group = source.add_mutually_exclusive_group()
    source_group.add_argument('-v', '--verbose', metavar="", help="displays more message")
    source.add_argument('status', help="displays git status messages", action="store_const", const="")
    args: Namespace = source.parse_args()

    # handles package creation
    if args.mkpkg:
        for i in args.mkpkg:
            create_package(i)  # loops through args and prints

    # handles file creation for function and normal python files
    if args.class_create:
        for i in args.class_create:
            create_parent_class(i)  # create python class files

    if args.function:
        for i in args.function:  # checks the arguments passed for function and creates the files in the list
            source_code_create(i)  # function that's creates the file and prototype if passed

    if args.touch:
        for i in args.touch:  # loops through the arguments passed and creates the files
            file_create(i)  # function that's creates the file
    if main_entr.is_git():  # returns True if git is installed in the machine else False see
        if main_entr.is_git_repo():  # checks if the current repo is a git repository and returns True
            # uses the -a switch to add files to git
            if args.add:
                for i in args.add:
                    main_entr.git_add(i) # calls the git add function
                # handles the git commit got tracked changes
                    if args.commit:  # checks if the -c switch is passed to the command line
                        # if args.add:  # checks if -a optional argument is passed
                        if args.commit:
                            msg = input("commit message: ")  # asks user for commit message and commit changes
                            if msg == "":
                                main_entr.git_commit()  # send default commit message if user passes no message whe prompted
                            else:
                                main_entr.git_commit(msg)
                        else:
                            main_entr.git_commit(str(args.commit))
                        # else:
                        #     print("run SC -a ('filenames') to add files before commit")

            # pushes changes to git
            if args.push:
                """calls the git push command to push changes"""
                main_entr.git_push()
            print(main_entr)  # prints "program ran successfully"
    else:
        print("Error Coming soon")


if __name__ == "__main__":
    main()
