#!/bin/bash

# Install pip
sudo apt-get update
sudo apt-get install python3-pip -y

# Install required Python packages
pip3 install pytelegrambotapi

# add next here
pip3 install Flask

echo "All dependencies installed successfully!"

