"""
test code for learning timeit,
to use run in terminal (on function sum() in this case) as:
'python -m timeit "total = sum(range(1000))"'

or code below is for testing from within app,
in this case time of 'setup' to 'statement' execution
for more info see book ch4 and docs:
https://docs.python.org/3/library/profile.html

TODO
write up test function to check which is faster for
item checking, set() versus list()
"""

from timeit import timeit
import random


def timeit_func():
    """checks time between setup
     and statement execution then prints it"""
    setup = 'from datetime import datetime'
    statement = 'datetime.now()'
    result = timeit(setup=setup, stmt=statement)
    print(f'Took an average of {result}ms')

timeit_func()


def sort_expensive():
    the_list = random.sample(range(1_000_000), 1_000)
    the_list.sort()

def sort_cheap():
    the_list = random.sample(range(1_000), 10)
    the_list.sort()
