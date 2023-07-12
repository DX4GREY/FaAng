#!/bin/bash

install_pip() {
    echo "Starting pip installation..."
    if [ -x "$(command -v pip)" ]; then
        echo "pip is already installed."
    else
        echo "Installing pip..."
        if [ -x "$(command -v python3)" ]; then
            sudo apt update
            sudo apt install python3-pip
        elif [ -x "$(command -v python)" ]; then
            sudo apt update
            sudo apt install python-pip
        fi
    fi
}

install_packages() {
    echo "Starting package installation using pip..."
    if [ -x "$(command -v pip)" ]; then
        echo "Installing PySocks..."
        python -m pip install PySocks

        echo "Installing colorama..."
        python -m pip install colorama

        echo "Installing requests..."
        python -m pip install requests

        echo "Package installation completed."
    else
        echo "pip is not installed. Cannot proceed with package installation."
    fi
}

run_faang_script() {
    echo "Installation success"
}

install_kali() {
    echo "Starting Python installation on Kali Linux..."
    sudo apt update
    sudo apt install python3
    python3 --version

    install_pip
    install_packages
    run_faang_script
}

install_termux() {
    echo "Starting Python installation on Termux..."
    pkg update
    pkg install python
    python --version

    install_pip
    install_packages
    run_faang_script
}

install_ubuntu() {
    echo "Starting Python installation on Ubuntu..."
    sudo apt update
    sudo apt install python3
    python3 --version

    install_pip
    install_packages
    run_faang_script
}

detect_platform() {
    platform=$(uname -o)
    case $platform in
        "Android")
            install_termux
            ;;
        "GNU/Linux")
            install_kali
            ;;
        "Ubuntu")
            install_ubuntu
            ;;
        *)
            echo "Unsupported platform: $platform"
            ;;
    esac
}

clear
echo "Automatic Platform Detection"
echo "============================"

detect_platform
