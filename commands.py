"""
This is the file where all of the commands that are going to be run exist

All commands must be unique subclasses of Commands and should overwrite root class vars and run method.
With this architecture the number of commands that can be run is mutable and the UI will adapt to
all existing DIRECT subclasses of Commands.
"""
import time
from pynput.keyboard import Key, Controller


# Abstract parent command class
# All commands to be run must be direct subclasses of this class.
class Commands:
    # Keyboard controller for pancake bot typing input
    keyboard = Controller()
    name = "Root"
    delay = 0  # seconds between executions
    priority = 1

    def run(self):
        pass


class HighLow(Commands):
    def __init__(self):
        self.name = "HighLow"
        self.delay = 40
        self.priority = 4

    def run(self):
        self.keyboard.type("p!highlow")
        self.keyboard.tap(Key.enter)
        time.sleep(1)
        self.keyboard.type("high")
        self.keyboard.tap(Key.enter)


class Fish(Commands):
    def __init__(self):
        self.name = "Fish"
        self.delay = 70
        self.priority = 3

    def run(self):
        self.keyboard.type("p!fish")
        self.keyboard.tap(Key.enter)


class Work(Commands):
    def __init__(self):
        self.name = "Work"
        self.delay = 310
        self.priority = 2

    def run(self):
        self.keyboard.type("p!work")
        self.keyboard.tap(Key.enter)


class Trivia(Commands):
    def __init__(self):
        self.name = "Trivia"
        self.delay = 610
        self.priority = 1

    def run(self):
        self.keyboard.type("p!trivia hard")
        self.keyboard.tap(Key.enter)
        time.sleep(1)
        self.keyboard.type("4")
        self.keyboard.tap(Key.enter)

