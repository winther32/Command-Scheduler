# Python Command Scheduler
by Mac Lyle

## Overview
Through a simple CLI, determines which commands to run and for how many minutes. Uses 2 threads, the scheduled commands and a simple progress bar.

This scheduler is ideal for afk farming via pynput control of mouse and keyboard.

## Making Commands
Making commands is super easy. In the commands.py file simply make a subclass of the Commands class and overwrite the inherited variables 
for name, delay, priority and the run method with whatever function you want to execute.

The name variable is what the UI will use to identify the command in the CLI.
Delay is seconds between executions of the function.
Priority determines order which the commands are to be executed if they are scheduled for the same time.
