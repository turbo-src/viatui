import pyautogui
import time
import os
from modules.screenshot_grid import create_screenshot_with_grid
from modules.screenshot_grid import create_screenshot
from modules.get_from_viatuix_config import get_from_viatuix_config

# Set the DISPLAY environment variable if necessary
os.environ['DISPLAY'] = ':1'

if __name__ == '__main__':
  # Click on settings menu (triple dots in a row)
  pyautogui.moveTo(1080, 8)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(50)
  screenshot.save('chromium-nix-screenshots/1.png')

  # Click on settings menu (triple dots in a row)
  pyautogui.moveTo(995, 95)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(50)
  screenshot.save('chromium-nix-screenshots/2.png')

  # Click on `Extensions`
  pyautogui.moveTo(725, 312)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(50)
  screenshot.save('chromium-nix-screenshots/3.png')

  # Click on `Manage Extensions`
  pyautogui.moveTo(550, 312)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(50)
  screenshot.save('chromium-nix-screenshots/4.png')

  # Switch 'Developer Mode' on
  pyautogui.moveTo(1000, 200)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(50)
  screenshot.save('chromium-nix-screenshots/5.png')

  # Click 'Load unpacked'
  pyautogui.moveTo(100 , 250)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(50)
  screenshot.save('chromium-nix-screenshots/6.png')

  # Click 'app' directory
  pyautogui.moveTo(50, 150)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(50)
  screenshot.save('chromium-nix-screenshots/7.png')

  # Click 'dist-chrome-extension
  pyautogui.moveTo(200, 130)
  pyautogui.doubleClick()
  time.sleep(2)
  pyautogui.moveTo(350, 50)
  pyautogui.click()
  pyautogui.press('enter')
  time.sleep(3)
  screenshot = create_screenshot_with_grid(50)
  screenshot.save('chromium-nix-screenshots/8.png')

  # Click extension button
  pyautogui.moveTo(850, 100)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/9.png')

  # Pin turbo-src extension
  pyautogui.moveTo(800, 250)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/10.png')

  # Get out of Extensions pin selection box
  pyautogui.press('esc')
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/11.png')

  # Make a new browser tab
  pyautogui.hotkey('ctrl', 't')
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/12.png')

  # Type in github url into bar
  login_page = get_from_viatuix_config('viatuix.json', 'url2')
  pyautogui.moveTo(200, 75)
  pyautogui.click()
  pyautogui.typewrite(login_page)
  time.sleep(2)
  pyautogui.press('enter')
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/13.png')

  # Type in username
  username = get_from_viatuix_config('viatuix.json', 'username')
  pyautogui.moveTo(414, 353)
  pyautogui.click()
  pyautogui.typewrite(username)
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/14.png')

  # Type in password
  password = get_from_viatuix_config('viatuix.json', 'password')
  pyautogui.moveTo(423, 425)
  pyautogui.click()
  pyautogui.typewrite(password)
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/15.png')

  # Submit username and password
  pyautogui.moveTo(502, 477)
  pyautogui.click()
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/16.png')

  # Don't save password
  pyautogui.moveTo(700, 400)
  pyautogui.click()
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/17.png')

  # Go to pulls page
  pyautogui.moveTo(300, 100)
  pyautogui.click()
  pulls_page = get_from_viatuix_config('viatuix.json', 'url3')
  pyautogui.typewrite(pulls_page)
  pyautogui.press('enter')
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/18.png')

  # Click on turbo-src extension
  pyautogui.moveTo(825, 100)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/19.png')

  # Click turbo-src 'continue with' button
  pyautogui.moveTo(600, 375)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/20.png')

  # Switch back to target page
  pyautogui.hotkey('alt', '2')
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/21.png')

  # Click on turbo-src extension
  pyautogui.moveTo(825, 100)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/22.png')

  # Click turbo-src 'continue to add repo to TurboSrc' button
  pyautogui.moveTo(700, 450)
  pyautogui.click()
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/23.png')

  ## Click turbo-src 'create repo' button
  #pyautogui.moveTo(700, 500)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/24.png')

  # Clear turbo-src popup
  pyautogui.press('esc')
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/25.png')

  # Load vote buttons (reload page)
  pyautogui.hotkey('ctrl', 'r')
  time.sleep(7)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/26.png')

  # Scroll down to see all vote buttons
  pyautogui.scroll(-2)
  time.sleep(3)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/27.png')