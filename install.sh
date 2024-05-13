#!/usr/bin/env bash
# handles the package installation

if [ "$(id -u)" != "0" ]
then
  echo "sorry, you are not root."
  exit 1
fi

MAIN_FILE="sc"
REQUIREMENTS="sub_func"

PROJECT_PATH="/opt/sc"
BIN_PATH="/usr/local/bin/"
MAN_PATH="/usr/local/share/man/man1/"

echo -e "Installing Binaries..."
sleep 09
mkdir -p "${PROJECT_PATH}"


cp "${MAIN_FILE}.py" "${PROJECT_PATH}/${MAIN_FILE}"
cp -r "${REQUIREMENTS}" "${PROJECT_PATH}"

echo -e "Making Executables"
sleep 03

chmod +x "${PROJECT_PATH}/${MAIN_FILE}"

ln -s "${PROJECT_PATH}/${MAIN_FILE}" "${BIN_PATH}/${MAIN_FILE}"

echo -e "Installing man pages.."

cp "man/sc.1" "${MAN_PATH}"

echo -e "Updating man database.."
sleep 03

mandb

echo -e "All set Run 'sc -h' for help or 'man sc' for more info "


