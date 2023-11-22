import pyautogui
from modules.screenshot_grid import create_screenshot_with_grid

# Set the DISPLAY environment variable if necessary
# os.environ['DISPLAY'] = ':1'

if __name__ == '__main__':
  screenshot = create_screenshot_with_grid(100)
  screenshot.save('screenshot.png')
