"""this module implements the necessary functions
   for git manipulation, creating repo, committing, staging changes pushing etc.
"""
import sys
import os
from git import Repo
import subprocess


class Git:
    """git class for git functionality and interaction"""
    path = os.getcwd()

    def __init__(self):
        """initialises at first call"""

    def is_git(self):
        """Checks if git is installed in the current directory
        """
        try:
            subprocess.check_output(['git', '--version'])
            return True
        except (FileNotFoundError, subprocess.CalledProcessError):
            return False

    def is_git_repo(self):
        """this checks if the current directory is a git directory
            :return True if success or false if not a git repo
        """
        git_folder = os.path.join(self.path, '.git')
        return os.path.isdir(git_folder)

    def create_repo(self, git_path):
        """initialises a new Repo
        returns an exception if fails and path is success
        Create an empty Git repository or reinitialize an existing one
        """
        if self.is_git_repo():
            return f"{self.path} is already a git repo"
        else:
            try:
                Repo.init(git_path)
                return f"Initialized empty Git repository in {git_path}"
            except Exception as e:
                return e

    def git_commit(self, message=f"added file"):
        """commits changes to the git and checks if message id null and
         Record changes to the repository
        if message is null it uses
        """
        subprocess.run(["git", "commit", "-m", f"{str(message)}"])

    def git_add(self, *args):
        """adds files to git repo/Add file contents to the index"""
        for file in args:
            result = subprocess.run(["git", "add", f"{file}"])
            if result.returncode == 0:
                print(f"added {file} to git")
            else:
                print(f"failed to add {file} to git")

    def __str__(self):
        """return successful operation with message Command Executed Successfully"""
        return f"program Executed Successfully"

    def git_push(self):
        """Update remote refs along with associated objects"""
        pushed = subprocess.run(["git", "push"])
        print(pushed.stdout)
