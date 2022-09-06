"""
test code to see how cProfile works, to test,
run in terminal (on file location) as:
'python -m cProfile --sort cumtime cpu_profiling.py'

https://docs.python.org/3/library/profile.html#module-cProfile
"""

import random
import time

def expensive_function():
    """takes up cycles"""
    execution_time = random.random() / 100
    time.sleep(execution_time)

if __name__ == '__main__':
    for _ in range(1000):
        expensive_function()
