#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    
    count = 0
    direction = 1
    for i in range(13):
        if direction == 1:         
            for j in range(12 - count):
                fill_cell()
                move_down()
                
            count += 1
            direction *= -1
            fill_cell()
            move_right()
        else:
            for j in range(12 - count):
                fill_cell()
                move_up()
            
            count += 1
            direction *= -1
            fill_cell()
            move_right()
            move_down()
            
    move_down()
    for i in range(13):
        move_left()
                 

if __name__ == '__main__':
    run_tasks()
