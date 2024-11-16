import pygetwindow as gw
import pyautogui
from PIL import Image
import numpy as np
import os

def determine_state(screenshot, threshold):
  # TODO: using the screenshot provided determine the state, i.e. in battle
  print(f"determining state")
  current_dir = os.getcwd()
  state_dir= os.path.join(current_dir, "../statescreenshots")
  state_images = []
  for filename in os.listdir(state_dir):
    state_images.append(os.path.join(state_dir, filename))
  for state_image_path in state_images:
    state_image = Image.open(state_image_path)
    if image_match(screenshot, state_image, threshold):
      return os.path.basename(state_image_path)
  return "no state detected"
def determine_action(state):
  # TODO: depending on the current state invoke an action type that will correctly handle it
  print(f"determine action")

def image_match(screenshot, state_image, threshold):
  #  TODO: find a way to compare these two images and if it is similar enough (based on threshhold) return true
  return False