#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_down()
    
    direction = 1
    for k in range(5):
        for i in range(3):
            if direction == 1:
                move_down()
                fill_cell()
                move_down()
                direction *= -1
            else:
                move_right()
                for j in range(2):
                    fill_cell()
                    move_up()
                
                fill_cell()
                move_right()
                direction *= -1
        
        direction *= -1
        move_up(2)
        if k != 4:
            move_right(2)
        else:
            move_left(2)
        

if __name__ == '__main__':
    run_tasks()
