#!/bin/bash

# Install pip
sudo apt-get update
sudo apt-get install python3-pip -y

# Install required Python packages
pip3 install python-telegram-bot

# add next here
# pip3 install ...

echo "All dependencies installed successfully!"

