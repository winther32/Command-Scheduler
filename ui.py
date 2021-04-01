import time
import logging as log
from pynput import keyboard
from commands import Commands


# Holds all of the UI functions and acts as form that stores the state of the user preferences
class Interface:
    def __init__(self):
        self.length = 0
        self.commands = []

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
    def get_commands(self):
        print("Select commands you wish to run:")
        for c in Commands.__subclasses__():
            cls = c()
            try:
                if str(input(cls.name + ": (y/n)")).lower() in "yes":
                    self.commands.append(cls)
            except ValueError:
                print("Error setting state flags. Quitting.")
                log.exception("Failed to get commands from user.")
                quit()

    # sets the state of the interface to user preset
    def set_state(self):
        self.get_runtime()
        self.get_commands()

    # method asking for user input to start
    @staticmethod
    def start():
        result = []  # wrapper for bool

        def on_press(key, decision=None):
            if decision is None:
                decision = result
            if key == keyboard.Key.enter:
                decision.append(True)
                return False  # stop the listener and release thread
            if key == keyboard.Key.esc:
                decision.append(False)
                # Stop listener w/exception
                return False

        print("Press Enter to begin or Esc to cancel.")
        # Collect events until released
        with keyboard.Listener(on_press=on_press) as listener:
            try:
                listener.join()
                if result[0]:
                    return True
                else:
                    print("Canceled")
                    return False
            except Exception:
                return False

    # begins a countdown in run console from 5
    @staticmethod
    def count_down():
        print("Starting output in 5 seconds!")
        for i in range(5):
            print("{}  ".format(5 - i), end="")
            time.sleep(1)
            print("\r", end="")
