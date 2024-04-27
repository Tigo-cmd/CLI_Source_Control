import os
import subprocess
from unittest.mock import patch

from sub_func.repo import Git
import unittest

# initialize git class for functionality
start = Git()


class test_installedGit(unittest.TestCase):
    def setUp(self):
        # Patch subprocess.check_output to avoid actual command execution during testing
        self.subprocess_check_output_patch = patch('subprocess.check_output')
        self.mock_subprocess_check_output = self.subprocess_check_output_patch.start()

    def tearDown(self):
        # Stop patching subprocess.check_output after each test
        self.subprocess_check_output_patch.stop()

    def test_git_installed(self):
        # Configure subprocess.check_output to return successfully
        self.mock_subprocess_check_output.return_value = b"git version 2.33.0"

        # Call the method under test
        result = start.is_git()

        # Assert that subprocess.check_output was called with the correct arguments
        self.mock_subprocess_check_output.assert_called_once_with(['git', ['--version']])

        # Assert the result
        self.assertTrue(result)

    def test_git_not_installed(self):
        # Configure subprocess.check_output to raise CalledProcessError
        self.mock_subprocess_check_output.side_effect = subprocess.CalledProcessError(returncode=1, cmd="git --version")

        # Call the method under test
        result = start.is_git()

        # Assert that subprocess.check_output was called with the correct arguments
        self.mock_subprocess_check_output.assert_called_once_with(['git', ['--version']])

        # Assert the result
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()