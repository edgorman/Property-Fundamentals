#!/usr/bin/env bash

# Update and install base packages
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade
sudo apt-get remove -y --purge man-db
sudo apt-get install -y build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev

# Fix for systems with nvidia gpus
sudo sed -i 's/quiet splash/quiet splash nouveau.modeset=0/g' /etc/default/grub

# Fix for swapspace being empty
sudo apt install swapspace -y

# Install python 3.10.*
cd /tmp
sudo wget https://www.python.org/ftp/python/3.10.6/Python-3.10.6.tgz
tar -xf Python-3.10.*.tgz
cd Python-3.10.*/
sudo ./configure --enable-optimizations
sudo make altinstall
sudo ln -sf /usr/local/bin/python3.10 /usr/bin/python

# Install npm 19.*
cd /tmp
curl -fsSL https://deb.nodesource.com/setup_19.x | sudo -E bash - &&\
sudo apt-get install -y nodejs
echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
