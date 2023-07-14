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
        
        echo "Installing httpx..."
        python -m pip install httpx
        
        echo "Installing undetected_chromedriver..."
        python -m pip install undetected_chromedriver
        
        echo "Installing cloudscraper..."
        python -m pip install cloudscraper
        
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
    
    DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
    mkdir -p $HOME/.faang
    cp $DIR/faang.py $HOME/.faang/faang.py
    echo "python $HOME/.faang/faang.py" | sudo tee /usr/local/bin/faang > /dev/null
    chmod +x /usr/local/bin/faang
}

install_termux() {
    echo "Starting Python installation on Termux..."
    pkg update
    pkg install python
    python --version

    install_pip
    install_packages
    run_faang_script

    mv "$(cd "$(dirname "$0")" && pwd)" $HOME/.faang
    echo "python $HOME/.faang" > $PREFIX/bin/faang
    chmod +x $PREFIX/bin/faang
}

install_ubuntu() {
    echo "Starting Python installation on Ubuntu..."
    sudo apt update
    sudo apt install python3
    python3 --version

    install_pip
    install_packages
    run_faang_script
    
    DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd)"
    mkdir -p $HOME/.faang
    cp $DIR/faang.py $HOME/.faang/faang.py
    echo "python $HOME/.faang/faang.py" | sudo tee /usr/local/bin/faang > /dev/null
    chmod +x /usr/local/bin/faang
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
echo "╔══╗────╔══╗───────  ╔══╗╔══╗───╔══╗\n║═╦╝╔═╗─║╔╗║╔═╦╗╔═╗  ╚╗╗║╚╗╗║╔═╗║══╣\n║╔╝─║╬╚╗║╠╣║║║║║║╬║  ╔╩╝║╔╩╝║║╬║╠══║\n╚╝──╚══╝╚╝╚╝╚╩═╝╠╗║  ╚══╝╚══╝╚═╝╚══╝\n────────────────╚═╝  ───────────────"
echo "============================"
echo "Waiting For Install"
sleep 3

detect_platform
