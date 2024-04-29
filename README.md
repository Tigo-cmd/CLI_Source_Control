# Command-Line Source Control (CLSC)
Welcome to CLSC, your command-line source control tool! CLSC is designed to simplify the management of your project's source code directly from your terminal. it's a user-friendly command-line source control tool designed to streamline your version control workflow. It empowers you to manage your code efficiently and collaboratively, directly from the terminal.

## Features:

- **Intuitive Commands**: Manage repositories with ease using simple commands.
- **Efficient Workflow**: Quickly commit changes, switch branches, and merge branches seamlessly.
- **Lightweight**: CLSC is designed to be fast and resource-efficient.
- **Cross-Platform**: Works smoothly on Windows, macOS, and Linux.
-- **Staging and Committing**: Stage specific files for inclusion in a commit and create meaningful commit messages.
-- **Lightweight and Efficient**: Operates efficiently from the command line, ideal for developers who prefer a streamlined experience.

-- offers a comprehensive set of commands for all your source control needs. Here's a quick overview:

    **init**: Initializes a new Git repository in the current directory.
    **status**: Shows the current status of your working directory and staging area.
    **add**: Adds files to the staging area for inclusion in the next commit.
    **commit**: Creates a new commit with a descriptive message.
    **branch**: Manages branches, including creating, listing, switching, and merging.
    **log**: Shows the commit history of your repository.
## Extra Feature:
-- **Create files: CLSC creates test startup files, python packages, py functions etc...


## Getting Started:

1. **Installation**:

   ```bash
   $ git https://github.com/Tigo-cmd/CLI_Source_Control.git
   $ cd CLI_Source_Control
   $ Run the script install.sh with sudo privileges to install ClSC on your computer
2. **Usage**:
   ```bash
   usage: SC [-h] [-t filename [filename ...]] [-t+ filename [filename ...]] [-a  [...]] [-c] [-p] [--version] [-v  | -s ]
   options:
     -h, --help            show this help message and exit
     -t filename [filename ...], --touch filename [filename ...]
                           creates files
     -t+ filename [filename ...], --function filename [filename ...]
                           creates files
     -a  [ ...], --add  [ ...]
                           add changes to the git
     -c, --commit          commits changes to the git
     -p , --push           Update remote refs along with associated objects
     --version             show program's version number and exit
     -v , --verbose        displays more message
     -s , -silence         displays limited messages


