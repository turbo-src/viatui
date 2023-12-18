
import pyautogui
import time
import os
from modules.screenshot_grid import create_screenshot_with_grid
from modules.screenshot_grid import create_screenshot
from modules.get_from_viatuix_config import get_from_viatuix_config

# Set the DISPLAY environment variable if necessary
os.environ['DISPLAY'] = ':1'

if __name__ == '__main__':
  # Click on pull request 5.
  pyautogui.moveTo(100, 285)
  pyautogui.click()
  time.sleep(5)
  screenshot = create_screenshot_with_grid(50)
  screenshot.save('chromium-nix-screenshots/tsrc-27.png')

  # Click on vote yes in popup modal for pull request 5.
  pyautogui.moveTo(400, 400)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(50)
  screenshot.save('chromium-nix-screenshots/tsrc-28.png')

  # Make popup modal go away.
  pyautogui.hotkey('ctrl', 'r')
  time.sleep(5)
  screenshot = create_screenshot_with_grid(50)
  screenshot.save('chromium-nix-screenshots/vote_merge_pull_request_5.png')