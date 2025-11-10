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
echo "Welcome to the Upd8All Updater ⚙ installer"
echo "========================================="
echo "Description: Upd8All is a versatile and comprehensive package update tool meticulously 
crafted to cater to the needs of Arch Linux users. No more worried about sudo, and continuous 
updating of the system with pacman, yay, and brew (You can even configure this as a service)."
echo "-------------------------------------------------------------"
echo "Creator/Engineer: Felipe Alfonso Gonzalez - github.com/felipealfonsog - f.alfonso@res-ear.ch"
echo "License: BSD 3-Clause (Restrictive: Ask about it)"
echo "Developed with love from Chile."
echo "***************************************************************************"

# Program name
pkgname="upd8all"
# Program version
pkgver="0.0.20"

# Repository URL
url="https://github.com/felipealfonsog/Upd8All"

# Download the source file from the URL
wget "$url/archive/refs/tags/v.$pkgver.tar.gz"


# Extract the source file
tar -xf "v.$pkgver.tar.gz"

# Install the Python script to /usr/local/bin
install -Dm755 "Upd8All-v.$pkgver/src/upd8all_updater.py" "/usr/local/bin/upd8all.py"

# Create a shell script to execute upd8all.py and copy it to /usr/local/bin
echo '#!/bin/bash' > upd8all
echo 'python /usr/local/bin/upd8all.py "$@"' >> upd8all
chmod +x upd8all
install -Dm755 upd8all "/usr/local/bin/upd8all"

# Clean up temporary files
rm -rf "v.$pkgver.tar.gz" "Upd8All-v.$pkgver"
rm -rf "upd8all"

echo "The upd8all program has been installed successfully."
