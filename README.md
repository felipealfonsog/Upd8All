## Upd8All 🔄 ⚙

Upd8All: Simplifying Package Updates for Arch Linux

Upd8All is a versatile and comprehensive package update tool meticulously crafted to cater to the needs of Arch Linux users. It provides a unified platform for managing package updates across various repositories, including both official Pacman repositories and the Arch User Repository (AUR),even Brew! empowering users to keep their systems up-to-date effortlessly.

<sub>* This is currently an experimental phase where the primary focus is on making the system functional and establishing a practical and logical pathway that aligns with both my vision and the project's goals. It might contain errors, bugs, etc. Many other non-core elements of the project are considered secondary.</sub>

![Version](https://img.shields.io/github/release/felipealfonsog/Upd8All.svg?style=flat&color=blue)
![Main Language](https://img.shields.io/github/languages/top/felipealfonsog/Upd8All.svg?style=flat&color=blue)
[![Open Source? Yes!](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)](https://github.com/Naereen/badges/)

[![BSD 3-Clause license](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

<!--
[![GPL license](https://img.shields.io/badge/License-GPL-blue.svg)](http://perso.crans.org/besson/LICENSE.html)
-->

[![Vim Powered](https://img.shields.io/badge/Vim-Powered-%2311AB00.svg?style=plastic&logo=vim&logoColor=white)](https://www.vim.org)
[![Visual Studio Code](https://badgen.net/badge/icon/Visual%20Studio%20Code?icon=visualstudio&label=)](https://code.visualstudio.com/)

#### Features

- Unified Package Management: Upd8All serves as a central hub for package management on Arch Linux systems. It seamlessly integrates with both Pacman and AUR repositories, allowing users to update all installed packages with ease. Whether updating essential system components or community-contributed packages, Upd8All offers a streamlined solution for maintaining software currency.

- Efficient Update Process: With Upd8All, updating packages on Arch Linux becomes a straightforward task. The tool automates the update process, enabling users to initiate updates with a single command. By handling privilege escalation and system updates intelligently, Upd8All ensures a smooth and hassle-free experience for users, minimizing manual intervention.

- Intuitive Command-Line Interface: Upd8All features an intuitive and user-friendly command-line interface designed to simplify package management tasks. Users can effortlessly check for available updates, perform package upgrades, and manage system software—all through simple and intuitive commands. Whether you're a seasoned Linux user or a newcomer, Upd8All makes package management accessible to everyone.

- Enhanced System Stability and Security: Keeping software up-to-date is crucial for maintaining system stability and security. Upd8All empowers users to stay ahead of potential vulnerabilities by providing timely updates for all installed packages. By ensuring that software components are patched and current, Upd8All contributes to a more secure and reliable computing environment for Arch Linux users.

#### New Features

- Added Feature: Implemented a function prompt_check_package_version() to inquire whether the user wishes to check a package version towards the end of the program.
- Enhancement: Adjusted the main() function to accommodate the functionality of prompting the user about checking a package version at the end of the program, thereby refining the program flow.
- Refinement: Eliminated the section of the code associated with the 1-minute timer, as it became redundant.
- Enhanced User Communication: Included print statements to provide users with updates on the program's progress and notify them when processes have been completed.

#

#### Screenshots

[![View Screenshot](https://img.shields.io/badge/View-Screenshot-green)](#)

#### Screenshot

<p align="center">
  <img src="./images/sshot.png" alt="Screenshot" width="400" height="350">
</p>

#

#### Installation
#### Via AUR using YAY

[![AUR](https://img.shields.io/aur/version/upd8all)](https://aur.archlinux.org/packages/upd8all)

<!-- 
[![AUR](https://img.shields.io/aur/version/upd8all.svg)](https://aur.archlinux.org/packages/upd8all)
-->

<!-- 
https://aur.archlinux.org/packages/upd8all
-->

Upd8All is available on AUR (Arch User Repository), and it can be installed using the `yay` package manager. Follow the steps below to install:

1. Make sure you have `yay` installed. If not, you can install it with the following command:
   
   ```
   sudo pacman -S yay
   ```
   Once yay is installed, you can install Term PDF by running the following command:
   
   ```
   yay -S upd8all
   ```
This command will automatically fetch the package from AUR and handle the installation process for you.

Then, run it with the following command:

```
apd8all
```

#### Cloning the Repository: 

 - Clone the Repository

```
git clone https://github.com/felipealfonsog/Upd8All.git
```

 - Navigate to the Directory:

```
cd Upd8All
```

 - Run the Bash Script:

```
bash execute.sh
```

 - Follow the Prompts:

When prompted, enter 'y' or 'Y' to run the update script.
If you wish to cancel, enter 'n' or 'N'.


 - Enjoy Upd8All:
Once the script finishes execution, your packages will be updated, and you'll be notified about any important updates.


#### 📝Important (Experimental Project)

[![Experimental Project](https://img.shields.io/badge/Project-Type%3A%20Experimental-blueviolet)](#)

This project is still in its experimental stage and may have limitations in terms of features and compatibility. Use at your own discretion.

#### 🤝 Support and Contributions

If you find this project helpful and would like to support its development, there are several ways you can contribute:

- **Code Contributions**: If you're a developer, you can contribute by submitting pull requests with bug fixes, new features, or improvements. Feel free to fork the project and create your own branch to work on.
- **Bug Reports and Feedback**: If you encounter any issues or have suggestions for improvement, please open an issue on the project's GitHub repository. Your feedback is valuable in making the project better.
- **Documentation**: Improving the documentation is always appreciated. If you find any gaps or have suggestions to enhance the project's documentation, please let me know.

[![Buy Me a Coffee](https://img.shields.io/badge/Buy%20Me%20a%20Coffee-%E2%98%95-FFDD00?style=flat-square&logo=buy-me-a-coffee&logoColor=black)](https://www.buymeacoffee.com/felipealfonsog)
[![PayPal](https://img.shields.io/badge/Donate%20with-PayPal-00457C?style=flat-square&logo=paypal&logoColor=white)](https://www.paypal.me/felipealfonsog)
[![GitHub Sponsors](https://img.shields.io/badge/Sponsor%20me%20on-GitHub-%23EA4AAA?style=flat-square&logo=github-sponsors&logoColor=white)](https://github.com/sponsors/felipealfonsog)

Your support and contributions are greatly appreciated! Thank you for your help in making this project better. If you need to mail me, this is the way: f.alfonso@res-ear.ch (I'm Felipe, the Computer Science Engineer behind this idea. Cheers!)

#### License

This project is licensed under the BSD 3-Clause License. See the [LICENSE](LICENSE) file for details.
