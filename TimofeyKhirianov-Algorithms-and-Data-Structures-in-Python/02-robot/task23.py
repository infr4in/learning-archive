#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    counter = 0
    while True:
        move_right()
        counter += 1
        
        if not wall_is_above():
            while not wall_is_above():
                move_up()
                fill_cell()
            
            while not wall_is_beneath():
                move_down()
                
        if wall_is_on_the_right():
            while counter != 0:
                move_left()
                counter -= 1
            
            break
        

if __name__ == '__main__':
    run_tasks()
