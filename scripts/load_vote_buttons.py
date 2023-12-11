import pyautogui
import time
import os
from modules.screenshot_grid import create_screenshot_with_grid
from modules.screenshot_grid import create_screenshot
from modules.get_from_viatuix_config import get_from_viatuix_config

# Set the DISPLAY environment variable if necessary
os.environ['DISPLAY'] = ':1'

if __name__ == '__main__':
  # Go to pulls page
  pyautogui.moveTo(300, 100)
  pyautogui.click()
  pulls_page = get_from_viatuix_config('viatuix.json', 'url3')
  pyautogui.typewrite(pulls_page)
  pyautogui.press('enter')
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/tsrc-18.png')

  # Click on turbo-src extension
  pyautogui.moveTo(825, 100)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/tsrc-19.png')

  # Click turbo-src 'continue with' button
  pyautogui.moveTo(600, 375)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/tsrc-20.png')

  # Switch back to target page
  pyautogui.hotkey('alt', '2')
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/tsrc-21.png')

  # Click on turbo-src extension
  pyautogui.moveTo(825, 100)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/tsrc-22.png')

  # Click turbo-src 'continue to add repo to TurboSrc' button
  pyautogui.moveTo(700, 450)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/tsrc-23.png')

  ## Click turbo-src 'create repo' button
  #pyautogui.moveTo(700, 500)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/tsrc-create-repo.png')

  # Clear turbo-src popup
  pyautogui.press('esc')
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/tsrc-24.png')

  # Load vote buttons (reload page)
  pyautogui.hotkey('ctrl', 'r')
  time.sleep(7)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/tsrc-25.png')

  # Scroll down to see all vote buttons
  pyautogui.scroll(-2)
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/tsrc-26.png')
