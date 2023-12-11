import pyautogui
import time
import os
from modules.screenshot_grid import create_screenshot_with_grid
from modules.screenshot_grid import create_screenshot
from modules.get_from_viatuix_config import get_from_viatuix_config

# Set the DISPLAY environment variable if necessary
os.environ['DISPLAY'] = ':1'

# Initialize parser
parser = argparse.ArgumentParser(description='Confim login')
# Adding argument
parser.add_argument('login_confirm', type=str, help='Login confirm')
# Parse arguments
args = parser.parse_args()

if __name__ == '__main__':
  login_page_2
  pyautogui.moveTo(400, 550)
  pyautogui.click()
  pyautogui.typewrite(args.login_confirm)
  time.sleep(2)
  pyautogui.press('enter')
  time.sleep(5)
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('chromium-nix-screenshots/login-confirm.png')
