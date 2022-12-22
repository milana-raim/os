#!/usr/bin/python3

import sys
import os
import time
import random

s = int(sys.argv[1])
pid = os.getpid()
parent_pid = os.getppid()

print(f"Child [{pid}]: I am started. PID {pid}. Parent PID {parent_pid}.")

time.sleep(s)

print(f"Child [{pid}]: I am ended. PID {pid}. Parent PID {parent_pid}.")

exit_status = random.randint(0, 1)
os._exit(exit_status)