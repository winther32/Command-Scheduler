import time
import logging as log
from pynput import keyboard


# Holds all of the UI functions and stores the state of the user preferences
class Interface:
    def __init__(self):
        self.length = 0
        self.highlow = False
        self.fish = False
        self.work = False
        self.trivia = False

    # prompts the user for input. returns input
    def get_runtime(self):
        while True:
            try:
                # attempt to convert input to int
                runtime = int(input("Enter how long to run in min: "))
            except ValueError:
                # retry if not valid
                print("Invalid. Must be an int.")
                continue
            else:
                # got an int. time to break and return
                self.length = runtime
                break

    # prompts user for which commands to run
    def flags(self):
        try:
            if str(input("highlow? (y/n) ")).lower() in "yes":
                self.highlow = True
            if str(input("fish? (y/n) ")).lower() in "yes":
                self.fish = True
            if str(input("work? (y/n) ")).lower() in "yes":
                self.work = True
            if str(input("trivia? (y/n) ")).lower() in "yes":
                self.trivia = True
        except ValueError:
            print("Error setting state flags. Quitting.")
            log.exception("Failed to set UI state flags")
            quit()

    # sets the state of the interface to user preset
    def set_state(self):
        self.get_runtime()
        self.flags()

    # method asking for user input to start
    @staticmethod
    def start():
        def on_press(key):
            if key == keyboard.Key.enter:
                time.sleep(.5)
                print("Starting output in 5 seconds!")
                for i in range(5):
                    print("{}  ".format(5 - i), end="")
                    time.sleep(1)
                    print("\r", end="")
                return False  # stop the listener and release thread

            if key == keyboard.Key.esc:
                # Stop listener w/exception
                raise Exception

        print("Press Enter to begin or Esc to cancel.")
        # Collect events until released
        with keyboard.Listener(
                on_press=on_press) as listener:
            try:
                listener.join()
            except Exception:
                quit()  # Gross but works to kill the process I guess...

