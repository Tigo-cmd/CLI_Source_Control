import unittest
import os
from sub_func.repo import Git
import subprocess

# initialize git class for functionality
start = Git()


class Test_gitrepo(unittest.TestCase):
    def test_is_gitrepo(self):
        """test if the current dir is a git repo"""
        # checks if the created folder is a git repo
        result = start.is_git_repo()
        self.assertTrue(result)

    def test_not_gitrepo(self):
        """test if the dir is not a git repository"""
        result = start.is_git_repo()

        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
