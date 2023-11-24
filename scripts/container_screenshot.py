import pyautogui
import time
from modules.screenshot_grid import create_screenshot_with_grid

# Set the DISPLAY environment variable if necessary
# os.environ['DISPLAY'] = ':1'

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
  pyautogui.moveTo(1000, 182)
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
  pyautogui.moveTo(200, 150)
  pyautogui.doubleClick()
  time.sleep(2)
  pyautogui.moveTo(350, 50)
  pyautogui.click()
  pyautogui.press('enter')
  time.sleep(3)
  screenshot = create_screenshot_with_grid(50)
  screenshot.save('chromium-nix-screenshots/8.png')

  ## Click extension button
  #pyautogui.moveTo(890, 60)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chrome-screenshot11.png')

  ## Pin turbo-src extension
  #pyautogui.moveTo(825, 212)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chrome-screenshot12.png')

  ## Get out of Extensions pin selection box
  #pyautogui.press('esc')
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chrome-screenshot13.png')

  ### Make a new browser tab
  #pyautogui.hotkey('ctrl', 't')
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chrome-screenshot14.png')

  ## Type in github url into bar
  #pyautogui.moveTo(200, 75)
  #pyautogui.click()
  #pyautogui.typewrite('github.com/7db9a/demo/pulls')
  #pyautogui.press('enter')
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/15.png')


  #######################################################
  # Useful info
  ######################################################
  ## See chrome console for debug
  #pyautogui.press('f12')
  #pyautogui.hotkey('ctrl', 'r')
  #pyautogui.moveTo(625, 100)
  #pyautogui.click()
  
