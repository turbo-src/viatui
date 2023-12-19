
import pyautogui
import time
import os
from modules.screenshot_grid import create_screenshot_with_grid
from modules.screenshot_grid import create_screenshot
from modules.get_from_viatuix_config import get_from_viatuix_config

# Set the DISPLAY environment variable if necessary
os.environ['DISPLAY'] = ':1'

if __name__ == '__main__':
  # Click on pull request 6.
  pyautogui.moveTo(100, 200)
  pyautogui.click()
  time.sleep(5)
  screenshot = create_screenshot_with_grid(50)
  screenshot.save('chromium-nix-screenshots/tsrc-30.png')

  # Click on vote yes in popup modal for pull request 6.
  pyautogui.moveTo(400, 400)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(50)
  screenshot.save('chromium-nix-screenshots/tsrc-31.png')

  # Make popup modal go away.
  pyautogui.hotkey('ctrl', 'r')
  time.sleep(5)
  screenshot = create_screenshot_with_grid(50)
  screenshot.save('chromium-nix-screenshots/tsrc-32.png')
