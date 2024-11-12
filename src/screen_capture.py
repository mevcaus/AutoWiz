import pygetwindow as gw
import pyautogui
from PIL import Image
import time
import os

def capture_window(window_title):
  try:
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
      print(f"Window with title '{window_title}' not found")
      return None
    window = windows[0]
    left, top = window.left, window.top
    width, height = window.width, window.height
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    current_dir = os.getcwd()
    save_path = os.path.join(current_dir, "screenshots")
    os.makedirs(save_path, exist_ok=True)
    file_path = os.path.join(save_path, f"screenshot_{timestamp}.png")
    screenshot.save(file_path)
    return screenshot

  except Exception as e:
    print(f"Error capturing screenshot: {str(e)}")
    return None