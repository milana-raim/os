#!/usr/bin/python

import os
import sys
import random


def run_child():
    child_pid = os.fork()
    if child_pid == 0:
        random_time = str(random.randint(5, 10))
        os.execl("./child.py", "child.py", random_time)
    print(f"Parent [{os.getpid()}]: I ran children process with PID {child_pid}.")

def main():
    number_children = int(sys.argv[1])

    for i in range(0, number_children):
        run_child()

    while number_children > 0:
        child_pid, exit_status = os.wait()
        exit_status = int(exit_status / 256)
        if child_pid != 0:
            print(f"Parent[{os.getpid()}]: Child with PID {child_pid} terminated. Exit Status {exit_status}.")
        if exit_status == 0:
            number_children = number_children - 1
        else:
            run_child()
            
main()
os._exit(os.EX_OK)