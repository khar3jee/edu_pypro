"""
change color counter to read line by line
add color file for testing
Prof Johnson for the file path win (adjunct profs, best profs)
"""

import os
import sys

#sys.path[0] - returns the path the python file is running in.
#os.path.join - concatenates the file with the file path

color_counts = {}
file_path = os.path.join(sys.path[0] + "\\" + "colors.txt")

with open(file_path) as favorite_colors_file:
    #favorite_colors = favorite_colors_file.read().splitlines()
    favorite_colors = []
    for line in favorite_colors_file: #.readlines():
        #print(line)
        favorite_colors.append(line.strip())
        #print(favorite_colors)

#print(favorite_colors)
for color in favorite_colors:
#    print(color)
    if color in color_counts:
        color_counts[color] += 1
    else:
        color_counts[color] = 1

print(color_counts)
