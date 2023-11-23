import pyautogui
import time
from modules.screenshot_grid import create_screenshot_with_grid

# Set the DISPLAY environment variable if necessary
# os.environ['DISPLAY'] = ':1'

if __name__ == '__main__':
  #print("Move to TurboSrc button")
  #pyautogui.moveTo(1200, 50)
  #time.sleep(1)
  #print("Click TurboSrc button")
  #pyautogui.click()
  #time.sleep(2)
  #print("Take screenshot of TurboSrc popup to identifiy 'Continue' button")
  #screenshot = create_screenshot_with_grid(100)
  #print("Saved screenshot screenshot: popup-continue-button.png")
  #screenshot.save('popup-continue-button.png')
  #pyautogui.click(1000, 350)
  #time.sleep(2)
  #screenshot = create_screenshot_with_grid(100)
  #print("Take screenshot of TurboSrc popup to identifiy 'Continue' button")
  #screenshot.save('popup-click-continue-button.png')
  #print("Saved screenshot screenshot: popup-click-continue-button.png")
  #print("Move to 'Create' button")
  #pyautogui.click(1000, 400)
  #time.sleep(2)
  #screenshot = create_screenshot_with_grid(100)
  #print("Take screenshot of TurboSrc after clicking 'Create' button")
  #screenshot.save('popup-after-click-continue-button.png')
  #print("Move to refresh button")
  pyautogui.moveTo(90, 50)
  pyautogui.click()
