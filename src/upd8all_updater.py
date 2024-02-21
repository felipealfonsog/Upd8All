import subprocess
import os
import getpass

def update_pacman():
    print("Updating Pacman packages...")
    command = "sudo pacman -Syu --noconfirm"
    execute_command_with_sudo(command)

def update_yay():
    print("Updating AUR packages with Yay...")
    command = "yay -Syu --noconfirm"
    execute_command_with_sudo(command)

def update_brew():
    print("Updating packages with Homebrew...")
    command = "brew update && brew upgrade"
    subprocess.run(command.split())

def check_gh_update():
    command = "brew info gh"
    output = subprocess.check_output(command.split()).decode("utf-8")
    lines = output.splitlines()
    for line in lines:
        if "stable" in line and "gh" in line:
            version = line.split()[1]
            print(f"The updated gh version is: {version}")

def execute_command_with_sudo(command):
    try:
        subprocess.run(command.split(), check=True)
    except subprocess.CalledProcessError:
        # Command failed, request sudo password and retry
        print("This command requires superuser privileges.")
        password = getpass.getpass(prompt="Enter sudo password: ")
        sudo_command = f"echo '{password}' | sudo -S {command}"
        subprocess.run(sudo_command, shell=True)

def main():
    update_pacman()
    update_yay()
    update_brew()
    check_gh_update()

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("This program requires superuser privileges to run.")
        exit(1)
    main()
