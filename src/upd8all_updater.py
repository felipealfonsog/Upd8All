import os
import sys
import getpass
import subprocess
import json

# Function to print the welcome message
def print_welcome_message():
    print("""
Welcome to the Upd8All Updater ⚙
=======================================
Description: Upd8All is a versatile and comprehensive package update tool meticulously 
crafted to cater to the needs of Arch Linux users. No more worries about sudo, and continuous 
updating of the system with pacman, yay, and brew.
-------------------------------------------------------------------------------------
Creator/Engineer: Felipe Alfonso Gonzalez - github.com/felipealfonsog - f.alfonso@res-ear.ch
License: BSD 3-Clause (Restrictive: Ask about it)
Developed with love from Chile.
*************************************************************************************
Default: Pacman, Yay, and Brew will be updated.
Press Enter to proceed or use the menu to modify.
""")

# Function to execute a command with sudo as needed
def execute_command_with_sudo(command, sudo_password):
    proc = subprocess.Popen(
        ["sudo", "-S", *command.split()],
        stdin=subprocess.PIPE,
        stdout=sys.stdout,
        stderr=sys.stderr,
        universal_newlines=True
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
    
    # Ensure the config directory for yay exists
    config_path = os.path.expanduser("~/.config/yay/")
    os.makedirs(config_path, exist_ok=True)
    
    # Create or update the yay config file
    config_file = os.path.join(config_path, "config.json")
    with open(config_file, "w") as f:
        json.dump({"misc": {"save": True}}, f)
    
    command = "yay -Syu --noconfirm"
    
    # Try running yay without sudo first
    try:
        result = subprocess.run(command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        print(result.stdout.decode())  # Print the output from yay
    except subprocess.CalledProcessError:
        # If yay fails, run it with sudo
        execute_command_with_sudo(command, sudo_password)

# Function to update packages with Homebrew
def update_brew():
    print("\nUpdating packages with Homebrew...")
    print("-------------------------------------")
    command = "brew update && brew upgrade"
    os.system(command)
    print("\n-----------------------------------\n")

# Function to display the menu and get user choice
def display_menu(yay_active, brew_active):
    print("\nSelect an option to configure Upd8All:")
    print("1. Update Pacman packages (active: yes)")
    print("2. Activate Update AUR packages with Yay (active: yes)" if yay_active else "2. Activate Update AUR packages with Yay (active: no)")
    print("3. Activate Homebrew packages (active: yes)" if brew_active else "3. Activate Homebrew packages (active: no)")
    print("4. Update all packages (default: press Enter)")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5) - If you are ready to continue just press Enter -: ")
    return choice.strip()

# Function to save configuration
def save_configuration(yay_active, brew_active):
    config_dir = os.path.expanduser("~/.upd8allconfig")
    os.makedirs(config_dir, exist_ok=True)
    
    config_file = os.path.join(config_dir, "config.cfg")
    with open(config_file, "w") as f:
        f.write(f"yay_active={'yes' if yay_active else 'no'}\n")
        f.write(f"brew_active={'yes' if brew_active else 'no'}\n")

# Function to load configuration
def load_configuration():
    config_dir = os.path.expanduser("~/.upd8allconfig")
    config_file = os.path.join(config_dir, "config.cfg")

    # Default values
    yay_active = True
    brew_active = True
    
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            for line in f:
                if "yay_active" in line:
                    yay_active = line.split('=')[1].strip() == 'yes'
                elif "brew_active" in line:
                    brew_active = line.split('=')[1].strip() == 'yes'
    
    return yay_active, brew_active

# Main function to run the update process
def main():
    # Print welcome message
    print_welcome_message()

    # Load previous configuration
    yay_active, brew_active = load_configuration()

    # Request sudo password at the start of the program
    while True:
        sudo_password = getpass.getpass(prompt="Enter your sudo password (press 'q' to quit): ")
        if sudo_password.lower() == 'q':
            print("Exiting the updater. Goodbye!")
            sys.exit(0)  # Exit the program immediately
        elif sudo_password:  # Check if password is not empty
            break
        else:
            print("Sudo password is required to continue. Please try again.")

    print()  # Add a newline after entering the password

    while True:
        choice = display_menu(yay_active, brew_active)

        if choice == '1':
            update_pacman(sudo_password)  # Update Pacman
        elif choice == '2':
            yay_active = not yay_active  # Toggle Yay activation
            status = "activated" if yay_active else "deactivated"
            print(f"Yay packages have been {status}.")
        elif choice == '3':
            brew_active = not brew_active  # Toggle Brew activation
            status = "activated" if brew_active else "deactivated"
            print(f"Homebrew packages have been {status}.")
        elif choice == '4' or choice == '':
            update_pacman(sudo_password)  # Always update Pacman
            if yay_active:
                update_yay(sudo_password)  # Update Yay if active
            if brew_active:
                update_brew()  # Update Brew if active
            print("\nAll packages have been updated.")
            save_configuration(yay_active, brew_active)  # Save the configuration
            print("Exiting the updater. Goodbye!")
            sys.exit(0)
        elif choice == '5':
            save_configuration(yay_active, brew_active)  # Save the configuration before exiting
            print("Exiting the updater. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
