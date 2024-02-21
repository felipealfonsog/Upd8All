import os
import sys

def print_welcome_message():
    print("""
Welcome to the Upd8All Updater
=======================================
Description:  is a multi-purpose package updater tool that streamlines the process 
of keeping packages updated on Arch Linux.
Creator: Felipe Alfonso Gonzalez - github.com/felipealfonsog - f.alfonso@res-ear.ch
License: BSD 3-Clause (Restrictive)
***************************************************************************
""")

def update_pacman():
    print("Updating Pacman packages...")
    print("-------------------------------------")
    command = "sudo pacman -Syu --noconfirm"
    os.system(command)

def update_yay():
    print("Updating AUR packages with Yay...")
    print("-------------------------------------")
    command = "yay -Syu --noconfirm"
    os.system(command)

def update_brew():
    print("Updating packages with Homebrew...")
    print("-------------------------------------")
    command = "brew update && brew upgrade"
    os.system(command)

def check_package_version(package, package_manager):
    if package_manager == "pacman":
        command = f"{package_manager} -Qi {package} | grep Version"
    elif package_manager == "yay":
        command = f"{package_manager} -Si {package} | grep Version"
    elif package_manager == "brew":
        command = f"{package_manager} info {package} | grep -E 'stable '"
    else:
        print(f"Package manager {package_manager} not recognized.")
        return
    
    print(f"Checking version of {package} using {package_manager}...")
    os.system(command)

def main():
    print_welcome_message()
    
    if os.geteuid() == 0:
        print("Error: Please do not run this script as root or using sudo.")
        sys.exit(1)
    update_pacman()
    update_yay()
    update_brew()
    
    package = input("Enter the name of the package to check its version (e.g., gh): ").strip().lower()
    package_manager = input("Enter the package manager (pacman, yay, brew): ").strip().lower()
    
    check_package_version(package, package_manager)

if __name__ == "__main__":
    main()
