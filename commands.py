import time
from pynput.keyboard import Key, Controller


# Class containing all of the info for executing a given command.
# These act as the processes that can be scheduled.
class Commands:
    # class variable that is the keyboard controller
    keyboard = Controller()

    # delays for the commands in sec
    HL_DELAY = 40
    FISH_DELAY = 70
    WORK_DELAY = 330
    TRIVIA_DELAY = 630

    # executes the highlow odds command
    # priority 4
    def odds(self):
        self.keyboard.type("p!highlow")
        self.keyboard.tap(Key.enter)
        time.sleep(1)
        self.keyboard.type("high")
        self.keyboard.tap(Key.enter)

    # executes the fishing command
    # priority 3
    # NOTE: since fishing rods break at random the only way to reliably use this is to have many rods in inv.
    def cast(self):
        self.keyboard.type("p!fish")
        self.keyboard.tap(Key.enter)

    # executes the work command
    # priority 2
    def job(self):
        self.keyboard.type("p!work")
        self.keyboard.tap(Key.enter)

    # executes the trivia command and deposit command
    # priority 1
    def knowledge(self):
        self.keyboard.type("p!trivia hard")
        self.keyboard.tap(Key.enter)
        time.sleep(1)
        self.keyboard.type("4")
        self.keyboard.tap(Key.enter)

        self.keyboard.type("p!dep all")
        self.keyboard.tap(Key.enter)
