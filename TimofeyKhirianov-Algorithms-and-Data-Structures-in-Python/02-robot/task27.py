#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    fill_cell()
        
    num = 1
    while True:   
        for _ in range(num):
            if wall_is_on_the_right():
                return
            
            move_right()

        fill_cell()
        num += 1       


if __name__ == '__main__':
    run_tasks()
