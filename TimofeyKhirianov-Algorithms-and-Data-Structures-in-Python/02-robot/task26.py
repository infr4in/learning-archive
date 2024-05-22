#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    counter = 9
    direction = 1
    for k in range(50):
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
        if k == 49:
            move_left(38)
            move_up(2)
            break
        
        if k == counter:
            move_left(38)
            move_down(2)
            counter += 10
        else:
            move_up(2)
            move_right(2)
            

if __name__ == '__main__':
    run_tasks()
