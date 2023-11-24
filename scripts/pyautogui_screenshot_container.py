import os
os.environ['DISPLAY'] = ':1'

import pyautogui

screenshot = pyautogui.screenshot()
screenshot.save('container_screenshot.png')
