import sched
import threading
from tqdm import tqdm

from ui import *
from commands import *


# starts a cli progress bar to display approximately where in the schedule execution is
def progress():
    for _ in tqdm(range(ui.length*60)):
        time.sleep(1)


# function that schedules all of the events to take place over duration given
# other args are what commands to schedule.
def schedule(duration, highlow=False, fish=False, work=False, trivia=False):
    s = sched.scheduler(time.time, time.sleep)
    c = Commands()
    sec = duration * 60

    if highlow:
        calls = sec // c.HL_DELAY
        for n in range(calls+1):
            s.enter(n * c.HL_DELAY, 4, c.odds)

    if fish:
        calls = sec // c.FISH_DELAY
        for n in range(calls+1):
            s.enter(n * c.FISH_DELAY, 3, c.cast)

    if work:
        calls = sec // c.WORK_DELAY
        for n in range(calls+1):
            s.enter(n * c.WORK_DELAY, 2, c.job)

    if trivia:
        calls = sec // c.TRIVIA_DELAY
        for n in range(calls+1):
            s.enter(n * c.TRIVIA_DELAY, 1, c.knowledge)

    if not s.empty():
        ui.start()

        t1 = threading.Thread(target=s.run, name="sched_commands")
        t2 = threading.Thread(target=progress, name="progress_bar")

        t1.start()
        t2.start()

        t1.join()
        t2.join()
    print("Done")


# Init ui
ui = Interface()
ui.set_state()
# init schedule as begin using usr inputs
schedule(ui.length, highlow=ui.highlow, fish=ui.fish, work=ui.work, trivia=ui.trivia)
