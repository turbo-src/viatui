import pyautogui
import time
from modules.screenshot_grid import create_screenshot_with_grid
from modules.get_from_viatuix_config import get_from_viatuix_config

# Set the DISPLAY environment variable if necessary
# os.environ['DISPLAY'] = ':1'

if __name__ == '__main__':
  ## Click on settings menu (triple dots in a row)
  #pyautogui.moveTo(1080, 8)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chromium-nix-screenshots/1.png')

  ## Click on settings menu (triple dots in a row)
  #pyautogui.moveTo(995, 95)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chromium-nix-screenshots/2.png')

  ## Click on `Extensions`
  #pyautogui.moveTo(725, 312)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chromium-nix-screenshots/3.png')

  ## Click on `Manage Extensions`
  #pyautogui.moveTo(550, 312)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chromium-nix-screenshots/4.png')

  ## Switch 'Developer Mode' on
  #pyautogui.moveTo(1000, 200)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chromium-nix-screenshots/5.png')

  ## Click 'Load unpacked'
  #pyautogui.moveTo(100 , 250)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chromium-nix-screenshots/6.png')

  ## Click 'app' directory
  #pyautogui.moveTo(50, 150)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chromium-nix-screenshots/7.png')

  ## Click 'dist-chrome-extension
  #pyautogui.moveTo(200, 150)
  #pyautogui.doubleClick()
  #time.sleep(2)
  #pyautogui.moveTo(350, 50)
  #pyautogui.click()
  #pyautogui.press('enter')
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(50)
  #screenshot.save('chromium-nix-screenshots/8.png')

  ## Click extension button
  #pyautogui.moveTo(850, 100)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/9.png')

  ## Pin turbo-src extension
  #pyautogui.moveTo(800, 250)
  #pyautogui.click()
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/10.png')

  ## Get out of Extensions pin selection box
  #pyautogui.press('esc')
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/11.png')

  ## Make a new browser tab
  #pyautogui.hotkey('ctrl', 't')
  #time.sleep(3)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/12.png')

  ## Type in github url into bar
  #pyautogui.moveTo(200, 75)
  #pyautogui.click()
  #pyautogui.typewrite('github.com/7db9a/demo/pulls')
  #pyautogui.press('enter')
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/13.png')

  ## Type in github url into bar
  #pyautogui.moveTo(200, 75)
  #pyautogui.click()
  #pyautogui.typewrite('github.com/login')
  #pyautogui.press('enter')
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/13.png')

  #ghusername = get_from_viatuix_config('viatuix.json', 'ghusername')
  #ghpassword = get_from_viatuix_config('viatuix.json', 'ghpassword')

  ## Type in username
  #pyautogui.moveTo(414, 353)
  #pyautogui.click()
  #pyautogui.typewrite(ghusername)
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/14.png')

  ## Type in password
  #pyautogui.moveTo(423, 425)
  #pyautogui.click()
  #pyautogui.typewrite(ghpassword)
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/15.png')

  ## Submit username and password
  #pyautogui.moveTo(502, 477)
  #pyautogui.click()
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/16.png')

  # Don't save password
  #pyautogui.moveTo(700, 400)
  #pyautogui.click()
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/17.png')

  ## Go to pulls page
  #pyautogui.moveTo(200, 75)
  #pyautogui.click()
  #pulls_page = get_from_viatuix_config('viatuix.json', 'url3')
  #pyautogui.typewrite(pulls_page)
  #pyautogui.press('enter')
  #time.sleep(5)
  #screenshot = create_screenshot_with_grid(100)
  #screenshot.save('chromium-nix-screenshots/18.png')

  #######################################################
  # Useful info
  ######################################################
  ## See chrome console for debug
  #pyautogui.press('f12')
  #pyautogui.hotkey('ctrl', 'r')
  #pyautogui.moveTo(625, 100)
  #pyautogui.click()

