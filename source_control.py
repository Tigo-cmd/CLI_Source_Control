#!/usr/bin/python3
from sub_func.repo import Git
from sub_func.create_func_files import source_code_create, file_create
from argparse import ArgumentParser, Namespace
import sys
import os

main_entr = Git()


def source_control():
    source = ArgumentParser(description="Command Line Source Control", prog="SC")
    source.add_argument('-t', '--touch', metavar="filename", nargs='+', help="creates files")
    source.add_argument('-t+', '--function', metavar="filename", nargs='+', help="creates files")
    source.add_argument('-a', '--add', metavar='', nargs='+', help="add changes to the git")
    source.add_argument('-c', '--commit', metavar='', help="commits changes to the git",
                        action="store_const", const="New Commit")
    source.add_argument('-p', '--push', metavar='', help="Update remote refs along with associated objects",
                        action="store_const", const="pushed")
    source.add_argument('--version', action='version', version="SC 1.0")
    source_group = source.add_mutually_exclusive_group()
    source_group.add_argument('-v', '--verbose', metavar="", help="displays more message")
    source_group.add_argument('-s', '-silence', metavar="", help="displays limited messages")
    args: Namespace = source.parse_args()

    # handles file creation for function and normal python files
    if args.function:
        for i in args.function:  # checks the arguments passed for function and creates the files in the list
            source_code_create(i)  # function that's creates the file and prototype if passed

    if args.touch:
        for i in args.touch:  # loops through the arguments passed and creates the files
            file_create(i)  # function that's creates the file

    # uses the -a switch to add files to git
    if args.add:
        for i in args.add:
            main_entr.git_add(i)  # calls the git add function

    # handles the git commit got tracked changes
    if args.commit:
        if args.add:
            if len(args.commit) == 0:
                msg = input("commit message: ")
                if msg == "":
                    main_entr.git_commit(args.commit)
                else:
                    main_entr.git_commit(msg)
            else:
                main_entr.git_commit(args.commit)
        else:
            print("run SC -a to add files before commit")

    # pushes changes to git
    if args.push:
        """calls the git push command to push changes"""
        main_entr.git_push()


#  main entry of the code, runs all functionalities
def main():
    if main_entr.is_git():
        if main_entr.is_git_repo():
            source_control()
            print(main_entr)
    else:
        print("Error Coming soon")


if __name__ == "__main__":
    main()
