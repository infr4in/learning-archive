#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    move_right()
    move_down()
    
    direction = 1
    for i in range(3):
        if direction == 1:
            move_down()
            fill_cell()
            move_down()
            direction *= -1
            move_right()
        else:
            for j in range(2):
                fill_cell()
                move_up()
            
            fill_cell()
            move_right()
            direction *= -1
    
    move_left(3)
    move_up(2)


if __name__ == '__main__':
    run_tasks()
