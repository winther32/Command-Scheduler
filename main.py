import sched
import threading
from tqdm import tqdm

from ui import *
from commands import *


# Starts a cli progress bar to display approximately progress of schedule execution
def progress():
    for _ in tqdm(range(ui.length*60)):
        time.sleep(1)


# Function that schedules and runs all of the events to take place over duration given
def schedule(duration, commands):
    s = sched.scheduler(time.time, time.sleep)
    sec = duration * 60

    for comm in commands:
        calls = sec // comm.delay
        for n in range(calls + 1):
            s.enter(n * comm.delay, comm.priority, comm.run)

    # Schedule a last event that occurs once duration has ended.
    # This kludge seems to prevent keyboard dump of commands from pynput at the end
    def last_event():
        print("Finishing up...")
    s.enter(sec + 2, 5, last_event)

    # print(s.queue)  # Debug to view what's been scheduled

    if not s.empty():
        t1 = threading.Thread(target=s.run, name="sched_commands")
        t2 = threading.Thread(target=progress, name="progress_bar")
        t1.start()
        t2.start()
        t2.join()
        t1.join()


# Driver code
ui = Interface()
ui.set_state()
if ui.start():
    ui.count_down()
    schedule(ui.length, ui.commands)
print("Done")
