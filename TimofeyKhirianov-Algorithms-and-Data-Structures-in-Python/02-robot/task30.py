#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    counter = 0
    while not wall_is_on_the_right():
        move_right()
        counter += 1
    
    while counter > 1:
        for i in range(counter-1):
            move_down()
            fill_cell()
        move_down()
        
        for i in range(counter-1):
            move_left()
            fill_cell()
        move_left()
        
        for i in range(counter-1):
            move_up()
            fill_cell()
        move_up()
        
        for i in range(counter-1):
            move_right()
            fill_cell()
        move_down()
        
        counter -= 2
    
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        move_left()
        

if __name__ == '__main__':
    run_tasks()
