#!/bin/bash

# Start Xvfb
Xvfb :1 -screen 0 1024x768x24 &

# Wait for Xvfb to start
while ! xdpyinfo -display :1 > /dev/null 2>&1; do
  sleep 0.1
done

# Start x11vnc
x11vnc -display :1 -forever -usepw -create &

# Start Fluxbox (or any other window manager)
fluxbox &

# Set the DISPLAY environment variable
export DISPLAY=:1

# Start Chromium in the background
chromium --no-sandbox --disable-dbus --disable-gpu --disable-software-rasterizer --disable-dev-shm-usage &

# Run script to interact with Chromium. Saves to 'chromium-nix-screenshots/'
~/.local/bin/poetry run python scripts/container_screenshot.py &

# Keep the script running
exec "$@"

