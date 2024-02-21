import os
import sys
import threading
import getpass
import subprocess

# Función para mostrar el mensaje de bienvenida
def print_welcome_message():
    print("""
Welcome to the Upd8All Updater
=======================================
Description: Upd8All is a versatile and comprehensive package update tool meticulously 
crafted to cater to the needs of Arch Linux users.
Creator: Felipe Alfonso Gonzalez - github.com/felipealfonsog - f.alfonso@res-ear.ch
License: BSD 3-Clause (Restrictive)
***************************************************************************
""")

# Función para verificar las dependencias del programa
def check_dependencies():
    print("Checking dependencies...")
    python_version = sys.version.split()[0]
    pip_version = subprocess.check_output(['pip', '--version']).decode().split()[1]
    print(f"Python {python_version}")
    print(f"pip {pip_version}")

    # Verificar si pip está instalado
    try:
        import some_package
    except ImportError:
        print("Installing required libraries using pip...")
        os.system(f"echo '{sudo_password}' | sudo -S pip install some_package")

# Funciones para actualizar los paquetes de Pacman, AUR con Yay y Homebrew
def update_pacman(sudo_password):
    print("Updating Pacman packages...")
    print("-------------------------------------")
    command = "pacman -Syu --noconfirm"
    execute_command_with_sudo(command, sudo_password)

def update_yay(sudo_password):
    print("Updating AUR packages with Yay...")
    print("-------------------------------------")
    command = "yay -Syu --noconfirm"
    execute_command_with_sudo(command, sudo_password)

def update_brew():
    print("Updating packages with Homebrew...")
    print("-------------------------------------")
    command = "brew update && brew upgrade"
    os.system(command)

# Función para ejecutar un comando con o sin sudo según sea necesario
def execute_command_with_sudo(command, sudo_password):
    if command.startswith("sudo"):
        os.system(f'echo "{sudo_password}" | {command}')
    else:
        os.system(command)

# Función para verificar la versión de un paquete en un gestor de paquetes específico
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

# Función que se ejecuta en un hilo separado para mostrar un mensaje de advertencia si no se ingresa un nombre de paquete en 1 minuto
def timeout_warning():
    print("Time's up. Program execution has ended.")
    sys.exit(0)

def main():
    # Verificar dependencias
    check_dependencies()

    # Mostrar mensaje de bienvenida
    print_welcome_message()

    # Solicitar la contraseña de sudo al inicio del programa
    sudo_password = getpass.getpass(prompt="Enter your sudo password: ")

    # Actualizar los paquetes
    update_pacman(sudo_password)
    update_yay(sudo_password)
    update_brew()

    # Iniciar hilo de temporización
    timer_thread = threading.Timer(60, timeout_warning)
    timer_thread.start()

    # Solicitar al usuario el nombre del paquete y el gestor de paquetes para verificar su versión
    package = input("Enter the name of the package to check its version (e.g., gh): ").strip().lower()
    if package.lower() == 'q':
        print("Program execution terminated by user.")
        sys.exit(0)
    
    package_manager = input("Enter the package manager (pacman, yay, brew): ").strip().lower()

    # Cancelar temporizador si el usuario proporciona un nombre de paquete
    timer_thread.cancel()

    # Verificar la versión del paquete especificado
    check_package_version(package, package_manager)

if __name__ == "__main__":
    main()
