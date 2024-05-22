#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_6():
    counter = 0
    while counter != 5:
        move_right()
        if cell_is_filled():
            counter += 1
        

if __name__ == '__main__':
    run_tasks()
