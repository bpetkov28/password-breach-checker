# password-breach-checker

## Overview

The Password Breach Checker is a program designed to help users determine if their passwords have been exposed in any data breaches. Users have the option to check passwords using a graphical user interface (GUI) for single password checks or a command-line interface (CLI) for checking multiple passwords simultaneously.

## Features
 - GUI Mode: Check a single password at a time using an easy-to-use graphical interface.
 - CLI Mode: Check multiple passwords at once using the command line for faster processing.
 - API Integration: Utilizes the API from pwnedpasswords.com to check if a password has been compromised.

## Getting Started

Prerequisites
- Python 3.x
- Required Python packages (can be installed via requirements.txt)

Installation

1. Clone the repository:

```bash
    git clone https://github.com/bpetkov28/password-breach-checker.git
```

2. Navigate to the project directory:

```bash
    cd password-breach-checker
```

3. Install the required packages:

```bash
    pip install -r requirements.txt
```

## Usage

GUI Mode
To start the program with the GUI, run the main.exe file located in the dist folder.

  - A window will appear allowing you to enter a single password.
  - Click the "Check" button to see if the password has been seen in any data breaches.

CLI Mode
To check multiple passwords quickly using the command line, use the following command:

```bash
    python pass_check.py password1 password2 password3 ...
```

  - Replace password1 password2 password3 ... with the actual passwords you want to check, separated by spaces.
  - The program will output the results for each password to the console.

## License
This project is licensed under the MIT License. See the 'LICENSE' file for details.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## Acknowledgments
  - Inspired by the need to help users ensure their passwords are secure.
  - Utilizes the "Have I Been Pwned" API for checking password breaches.

##
Thank you for using the Password Breach Checker! Stay safe and secure online.