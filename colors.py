"""
x change color counter to read line by line
x add color file for testing
Prof Johnson for the file path win (adjunct profs, best profs)
new issue, check data to produce unique color set
"""

import os
import sys
from typing import KeysView

#sys.path[0] - returns the path the python file is running in.
#os.path.join - concatenates the file with the file path


color_counts = {}
FILE_PATH = os.path.join(sys.path[0] + "\\" + "colors.txt")

def open_file():
    """opens and reads files outputs a list"""
    with open(FILE_PATH) as favorite_colors_file:
    #favorite_colors = favorite_colors_file.read().splitlines()
        #favorite_colors = []
        favorite_colors = set()
        for line in favorite_colors_file: #.readlines():
            #print(line)
            favorite_colors.add(line.strip())
            #print(favorite_colors)
        return favorite_colors
fav_colors = open_file()

def color_sort(color_list):
    """sort items based off a list and add to a dict"""
    for color in color_list:
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
    return color_counts

def check_list(sought_item, item_list):
    return sought_item in item_list

#print(set(color_sort(open_file()).keys()))
# ^screwing around^
#print('green' in color_counts)
#print('green' in favorite_colors)
print(check_list('green', fav_colors))
