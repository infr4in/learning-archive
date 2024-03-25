#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()
    direction = 1
    for i in range(12):
        if direction == 1:
            for j in range(26):
                fill_cell()
                move_right()
            direction *= -1
        else:
            for j in range(26):
                fill_cell() 
                move_left()
            direction *= -1
        
        fill_cell()
        move_down()


if __name__ == '__main__':
    run_tasks()
