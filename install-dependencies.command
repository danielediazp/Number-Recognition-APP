# @file install-dependencies.command
# @author Robert Oganesian (roganesian@uri.edu)
# @version 1.0
# @date 2022-12-04

#! /bin/bash

if ! command -v brew ; then
    # Install Homebrew
    printf "Homebrew was not found... beginning installation!\n"
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "Brew was found... updating!\n"
    brew update
fi

# Install python3, pip3, and git
brew install python3
brew install git

# Install python packages tensorflow, opencv, numpy, clustimage, tkinter, and termcolor
pip3 install tensorflow
pip3 install opencv-python
pip3 install numpy
pip3 install clustimage
pip3 install tkinter
pip3 install termcolor

# Install pygame for the GUI inerface
pip3 install pygame

printf "\n--- Dependencies installed! ---"
printf "\nFor Uninstall directions, visit: https://mac.install.guide/homebrew/5.html"