#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    counter = 1
    direction = 1
    while not wall_is_beneath():
        if direction == 1:
            while not wall_is_on_the_right():
                fill_cell()
                move_right()
            
            counter += 1
            direction *= -1
            fill_cell()
            move_down()
        else:
            while not wall_is_on_the_left():
                fill_cell()
                move_left()
            
            counter += 1
            direction *= -1
            fill_cell()
            move_down()
    
    if counter % 2 == 0:
        while not wall_is_on_the_left():
            fill_cell()
            move_left()
        fill_cell()
    else:
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
        fill_cell()
        
        while not wall_is_on_the_left():
            move_left()


if __name__ == '__main__':
    run_tasks()
