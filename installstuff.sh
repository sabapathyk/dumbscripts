#!/bin/bash

# Sources and stuff
sed -i 's/in.archive/archive/g' /etc/apt/sources.list

# Install essentials
apt-get -y install curl git cryptsetup zsh awesome

# Install entertainment packages
apt-get -y install moc 

# Install graphical packages 
apt-get -y install gimp inkscape libreoffice zathura

# Install Dev packages
apt-get -y install ipython

# Virt packages
apt-get -y install kvm virt-manager virtualbox-ose

# Other packages
apt-get -y install vlc mpd

git config --global user.name "My name"
git config --global user.email "myemail@domain.com"
