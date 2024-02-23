import os
import sys
import getpass
import subprocess
import json
import time

# Function to print the welcome message
def print_welcome_message():
    print("""
Welcome to the Upd8All Updater ⚙
=======================================
Description: Upd8All is a versatile and comprehensive package update tool meticulously 
crafted to cater to the needs of Arch Linux users. No more worried about sudo, and continuous 
updating of the system with pacman, yay, and brew (Suited my needs).
-------------------------------------------------------------------------------------
Creator/Engineer: Felipe Alfonso Gonzalez - github.com/felipealfonsog - f.alfonso@res-ear.ch
License: BSD 3-Clause (Restrictive: Ask about it)
Developed with love from Chile.
*************************************************************************************
""")

# Function to execute a command with sudo as needed
def execute_command_with_sudo(command, sudo_password):
    # Set environment variable to prevent sudo from asking for password
    env = os.environ.copy()
    env['SUDO_ASKPASS'] = '/bin/false'
    
    proc = subprocess.Popen(
        ["sudo", "-S", *command.split()],
        stdin=subprocess.PIPE,
        stdout=sys.stdout,
        stderr=sys.stderr,
        universal_newlines=True,
        env=env  # Pass the modified environment variable
    )

    # Send sudo password
    proc.stdin.write(sudo_password + '\n')
    proc.stdin.flush()

    # Wait for the process to complete
    proc.communicate()
    if proc.returncode != 0:
        print(f"Error executing command with sudo: {command}")
        sys.exit(1)

# Function to update Pacman packages
def update_pacman(sudo_password):
    print("\nUpdating Pacman packages...")
    print("-------------------------------------")
    command = "pacman -Syu --noconfirm"
    execute_command_with_sudo(command, sudo_password)

# Function to update AUR packages with Yay
def update_yay(sudo_password):
    print("\nUpdating AUR packages with Yay...")
    print("-------------------------------------")
    config_path = os.path.expanduser("~/.config/yay/")
    os.makedirs(config_path, exist_ok=True)
    config_file = os.path.join(config_path, "config.json")
    with open(config_file, "w") as f:
        json.dump({"misc": {"save": True}}, f)
  
    command = "yay -Syu --noconfirm"
    
    # Check if sudo is required for the Yay command
    need_sudo = False
    try:
        subprocess.run(command.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
    except subprocess.CalledProcessError:
        need_sudo = True
    
    if need_sudo:
        # Execute the Yay command with sudo if necessary
        execute_command_with_sudo(command, sudo_password)
    else:
        # Execute the Yay command directly without sudo
        os.system(command)

# Function to update packages with Homebrew
def update_brew():
    print("\nUpdating packages with Homebrew...")
    print("-------------------------------------")
    command = "brew update && brew upgrade"
    os.system(command)
    print("\n-----------------------------------\n")

# Function to check the version of a package in a specific package manager
def check_package_version(package, package_manager):
    if package_manager == "pacman":
        command = f"pacman -Qi {package} | grep Version"
    elif package_manager == "yay":
        command = f"yay -Si {package} | grep Version"
    elif package_manager == "brew":
        command = f"brew info {package} | grep -E 'stable '"
    else:
        print(f"Package manager {package_manager} not recognized.")
        return
    
    print(f"Checking version of {package} using {package_manager}...")
    os.system(command)

def main():
    # Print welcome message
    print_welcome_message()

    # Check if the user has yay installed
    try:
        subprocess.run(["yay", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        has_yay = True
    except FileNotFoundError:
        has_yay = False

    # Check if the user has Homebrew installed
    try:
        subprocess.run(["brew", "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        has_brew = True
    except FileNotFoundError:
        has_brew = False

    # Request sudo password at the start of the program
    sudo_password = getpass.getpass(prompt="Enter your sudo password: ")
    print()  # Add a newline after entering the password

    # Update packages
    update_pacman(sudo_password)

    if has_yay:
        update_yay(sudo_password)
    else:
        print("You do not have Yay installed.")

    if has_brew:
        update_brew()
    else:
        print("You do not have Brew installed.")

    # Inform the user about program termination after 1 minute of inactivity
    print("\nNote: If no further input is provided within 1 minute, the program will terminate.\n")

    # Request package name and package manager to check its version
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= 60:
            print("\nTime's up. Program execution has ended.\n")
            break

        print("Select the package manager to check the version:")
        print("1. Pacman")
        if has_yay:
            print("2. Yay")
        if has_brew:
            print("3. Brew")

        selected_option = input("Enter the option number (e.g., 1) or 'q' to quit: ").strip().lower()

        # Check if the user wants to quit
        if selected_option == 'q':
            print("\nExiting the program.\n")
            break

        package_manager = ""
        if selected_option == '1':
            package_manager = "pacman"
        elif selected_option == '2' and has_yay:
            package_manager = "yay"
        elif selected_option == '3' and has_brew:
            package_manager = "brew"
        else:
            print("\nInvalid option. Please enter a valid option number or 'q' to quit.\n")
            continue

        # Request package name
        package = input("Enter the name of the package to check its version (e.g., gh): ").strip().lower()

        # Check the version of the specified package
        check_package_version(package, package_manager)
        break

if __name__ == "__main__":
    main()
