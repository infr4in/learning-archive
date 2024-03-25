#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    while True:
        if not wall_is_above() and not wall_is_beneath():
            move_up()
            fill_cell()
            move_down(2)
            fill_cell()
            move_up()
        elif not wall_is_above():
            move_up()
            fill_cell()
            move_down()
        elif not wall_is_beneath():
            move_down()
            fill_cell()
            move_up()
        elif wall_is_above() and wall_is_beneath():
            fill_cell()
            
        if wall_is_on_the_right():
            break
        else:
            move_right()


if __name__ == '__main__':
    run_tasks()
