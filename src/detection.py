mport pygetwindow as gw
import pyautogui
from PIL import Image
import numpy as np
import time
import os

#Notes: determine state determines players state, passes down state to determine action, which determines the function to be used


def determine_state(screenshot, threshold):
  # TODO: using the screenshot provided determine the state, i.e. in battle
  print(f"determine state")




def determine_action(state):
  # TODO: depending on the current state invoke an action type that will correctly handle it  print(f"determine action")

  actions = {
    "sell": handle_sell,
    "move_to_quest": handle_move_to_quest,
    "use_spell": handle_use_spell,
  }

  action = actions.get(state, handle_unknown_state)
  action()


def handle_sell():
  print("selling items")
  #TODO: open inventory, select item, sell


def handle_move_to_quest():
  print("moving to quest")
  #TODO: walk towards whereever arrow is pointing.

def handle_use_spell():
  print("using spell")
  # TODO: have list of spells to refrence for bot to use, maybe with priority
  select_spell("path/to/spell_image.png")

  def handle_unknown_state():
    print("Unknown state: no action taken")

def select_spell(spell_image_path):
    """
    Selects a spell on the screen by matching a provided spell image.
    """
    try:
        spell_location = pyautogui.locateOnScreen(spell_image_path, confidence=0.9)
        if spell_location:
            pyautogui.moveTo(spell_location.left + spell_location.width / 2,
                             spell_location.top + spell_location.height / 2)
            pyautogui.click()
            print(f"Spell used: {spell_image_path}")
        else:
            print(f"Spell {spell_image_path} not found on screen.")
    except Exception as e:
        print(f"Error using spell: {str(e)}")