import pyautogui
import time
import os
import argparse
from modules.screenshot_grid import create_screenshot_with_grid
from modules.screenshot_grid import create_screenshot
from modules.get_from_viatuix_config import get_from_viatuix_config

# Set the DISPLAY environment variable if necessary
os.environ['DISPLAY'] = ':1'

# Initialize parser
parser = argparse.ArgumentParser(description='Take a screenshot and save it with a given filename.')
# Adding argument
parser.add_argument('filename', type=str, help='Filename to save the screenshot')
# Parse arguments
args = parser.parse_args()

if __name__ == '__main__':
    dir = 'chromium-nix-screenshots'
    # Load vote buttons (reload page) and save screenshot.
    pyautogui.hotkey('ctrl', 'r')
    time.sleep(3)
    screenshot = create_screenshot_with_grid(100)
    # Use the filename from the command line argument
    screenshot.save(os.path.join(dir, args.filename))
