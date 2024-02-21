import os
import sys

def update_pacman():
    print("Updating Pacman packages...")
    command = "sudo pacman -Syu --noconfirm"
    os.system(command)

def update_yay():
    print("Updating AUR packages with Yay...")
    command = "yay -Syu --noconfirm"
    os.system(command)

def update_brew():
    print("Updating packages with Homebrew...")
    command = "brew update && brew upgrade"
    os.system(command)

def check_gh_update():
    try:
        command = "brew info gh"
        output = os.popen(command).read()
        lines = output.splitlines()
        for line in lines:
            if "stable" in line and "gh" in line:
                version = line.split()[1]
                print(f"The updated gh version is: {version}")
    except Exception as e:
        print(f"Error checking gh update: {e}")

def main():
    if os.geteuid() == 0:
        print("Error: Please do not run this script as root or using sudo.")
        sys.exit(1)
    update_pacman()
    update_yay()
    update_brew()
    check_gh_update()

if __name__ == "__main__":
    main()
