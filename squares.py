"""
build a generator for squares
"""

NUM_LIST = [1, 2, 3, 4, 5, 6, 7, 8]

def squares():
    """given list of integers return the squares"""
    for i in NUM_LIST:
        yield i ** 2

sq_gen = squares()

#print(type(sq_gen))
for i in sq_gen:
    print(i)
