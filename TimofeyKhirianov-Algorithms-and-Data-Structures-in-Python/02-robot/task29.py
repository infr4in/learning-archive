#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    counter = 0
    while counter != 3:
        move_right()
        if wall_is_on_the_right():
            break
        elif not cell_is_filled():
            counter = 0
        else:
            counter += 1


if __name__ == '__main__':
    run_tasks()
