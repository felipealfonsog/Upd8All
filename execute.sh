#!/bin/bash

#*************************************
# Upd8All : is a multi-platform package 
# updater tool that streamlines the process 
# of keeping packages updated on Arch Linux.
#*************************************
# Developed and engineered by 
# Felipe Alfonso Gonzalez <f.alfonso@res-ear.ch>
# Computer Science Engineer
# Chile
#*************************************


echo "


░█─░█ █▀▀█ █▀▀▄ ▄▀▀▄ ─█▀▀█ █── █── 
░█─░█ █──█ █──█ ▄▀▀▄ ░█▄▄█ █── █── 
─▀▄▄▀ █▀▀▀ ▀▀▀─ ▀▄▄▀ ░█─░█ ▀▀▀ ▀▀▀


  ╔═══════════════════════════════════════╗
  ║                                       ║
  ║   ~ Upd8All ~                         ║
  ║   Developed with ❤️ by                 ║
  ║   Felipe Alfonso González L.          ║
  ║   Computer Science Engineer           ║
  ║   Chile                               ║
  ║                                       ║
  ║   Contact: f.alfonso@res-ear.ch       ║
  ║   Licensed under BSD v3               ║
  ║   GitHub: github.com/felipealfonsog   ║
  ║   LinkedIn:                           ║
  ║   linkedin.com/in/felipealfonsog      ║
  ║                                       ║
  ╚═══════════════════════════════════════╝


"

# Welcome and program details
echo "Welcome to the Upd8All Updater"
echo "======================================="
echo "Description:  is a multi-platform package updater tool that streamlines the process of keeping packages updated on Arch Linux."
echo "Creator: Felipe Alfonso Gonzalez - github.com/felipealfonsog - f.alfonso@res-ear.ch"
echo "License: BSD v3 (Restrictive)"
echo "***************************************************************************"
echo ""

PYTHON_SCRIPT="./src/upd8all_updater.py"

# check if any python installed or not

wherepython () {
	if ! command -v "python" > /dev/null ; then
	echo "Sorry, it looks like Python isn't installed."
	echo "please check Python installed / working perfectly"
	sleep 2
	exit 0
else 
 
	echo "Possible python locations"
	echo ""
	whereis python
	echo ""
fi
}

# main works

wherepython

# Check if Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "Error: Python script not found at $PYTHON_SCRIPT"
    exit 1
fi

# Ask user if they want to continue
read -p "Do you want to run the update script? (y/n): " choice
case "$choice" in 
  y|Y ) 
    # Execute Python script
    python3 "$PYTHON_SCRIPT"
    ;;
  n|N ) 
    echo "Update script cancelled."
    ;;
  * ) 
    echo "Invalid choice. Please enter 'y' or 'n'."
    ;;
esac
