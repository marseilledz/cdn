#!/bin/bash

# Start the X server in fullscreen mode
X :0 -screen 0 1024x768x24 &
sleep 5

# Run the Python script
python3 /home/your_username/hello_tk.py

# Stop the X server
killall Xorg
