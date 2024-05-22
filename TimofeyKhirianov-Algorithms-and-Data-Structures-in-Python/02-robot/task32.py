#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    counter = 0
    while not wall_is_on_the_right():
        if wall_is_above() and wall_is_beneath():
            fill_cell()
        
        if not wall_is_above():
            while not wall_is_above():
                move_up()
                if not cell_is_filled():
                    fill_cell()
                else:
                    counter += 1
            
            while not wall_is_beneath():
                move_down()
                
        move_right()
    
    mov("ax", counter)
                

if __name__ == '__main__':
    run_tasks()
