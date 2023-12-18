
import pyautogui
import time
import os
from modules.screenshot_grid import create_screenshot_with_grid
from modules.screenshot_grid import create_screenshot
from modules.get_from_viatuix_config import get_from_viatuix_config

# Set the DISPLAY environment variable if necessary
os.environ['DISPLAY'] = ':1'

if __name__ == '__main__':
  ## Click on pull request 5.
  #pyautogui.moveTo(100, 285)
  #pyautogui.click()
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chromium-nix-screenshots/tsrc-27.png')

  ## Click on vote yes in popup modal for pull request 5.
  #pyautogui.moveTo(400, 400)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chromium-nix-screenshots/tsrc-28.png')

  ### notes below

  ## Click on settings menu (triple dots in a row)
  #pyautogui.moveTo(995, 95)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chromium-nix-screenshots/tsrc-2.png')

  ## Click on `Extensions`
  #pyautogui.moveTo(725, 312)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chromium-nix-screenshots/tsrc-3.png')

  ## Click on `Manage Extensions`
  #pyautogui.moveTo(550, 312)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chromium-nix-screenshots/tsrc-4.png')

  ## Switch 'Developer Mode' on
  #pyautogui.moveTo(1000, 200)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chromium-nix-screenshots/tsrc-5.png')

  ## Click 'Load unpacked'
  #pyautogui.moveTo(100 , 250)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chromium-nix-screenshots/tsrc-6.png')

  ## Click 'app' directory
  #pyautogui.moveTo(50, 150)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chromium-nix-screenshots/tsrc-7.png')

  ## Click 'dist-chrome-extension
  #pyautogui.moveTo(200, 130)
  #pyautogui.doubleClick()
  #time.sleep(2)
  #pyautogui.moveTo(350, 50)
  #pyautogui.click()
  #pyautogui.press('enter')
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chromium-nix-screenshots/tsrc-8.png')

  ## Click extension button
  #pyautogui.moveTo(850, 100)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/tsrc-9.png')

  ## Pin turbo-src extension
  #pyautogui.moveTo(800, 250)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/tsrc-10.png')

  ## Get out of Extensions pin selection box
  #pyautogui.press('esc')
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/tsrc-11.png')
