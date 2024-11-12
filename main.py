from src.screen_capture import capture_window
from src.config import WINDOW_TITLE, THRESHHOLD
from src.detection import determine_state, determine_action

def main():
  screenshot = capture_window(WINDOW_TITLE)
  state = determine_state(screenshot, THRESHHOLD)


if __name__ == "__main__":
  main()