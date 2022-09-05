"""
Numbers and counting
Change the functions into more efficient ones
(write up what I learned with functions from collections)
https://docs.python.org/3/library/collections.html#collections.defaultdict
"""

from collections import Counter

num_list = [1, 2, 3, 4, 5, 6, 3, 7, 8, 9, 10, 11, 3, 12, 8, 13, 14, 7, 15]

def get_number_with_highest_count(counts):  # <1>
    return max(
        counts,
        key=lambda number: counts[number]
    )


def most_frequent(numbers):
    counts = Counter(numbers)

    return get_number_with_highest_count(counts)

print(most_frequent(num_list))
