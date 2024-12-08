import pandas as pd
from copy import deepcopy
UP = [-1,0]
DOWN = [1,0]
LEFT = [0,-1]
RIGHT = [0,1]


clockwise = [UP, RIGHT, DOWN, LEFT]
with open('inputs/in6.txt') as file:
    area = []
    for x in file:
        x = x.strip()
        line = []
        for y in x:
            line.append(y)
        area.append(line)

for row in range(len(area)):
    for col in range(len(area[row])):
        if(area[row][col] == '^'):
            start_row = row
            start_col = col
            begin_row = row
            begin_col = col
copy_area = deepcopy(area)
direction = clockwise[0]

part1_nodes = []


while start_row >= 0 and start_col >= 0 and start_row < len(area) and start_col < len(area[start_row]):
    if area[start_row][start_col] != '#':
        area[start_row][start_col] = 'X'
        start_row = start_row + direction[0]
        start_col = start_col + direction[1]
    else:
        start_row = start_row - direction[0]
        start_col = start_col - direction[1]
        if clockwise.index(direction) < len(clockwise) - 1:
            direction = clockwise[clockwise.index(direction)+1]
        else:
            direction = clockwise[0]
        start_row = start_row + direction[0]
        start_col = start_col + direction[1]

count = 0
for row in range(len(area)):
    for col in range(len(area[row])):
        if(area[row][col] == 'X'):
            count += 1
            part1_nodes.append([row, col])

part1_nodes.remove([begin_row, begin_col])
print("Deel 1: " + str(count))

grid_height = len(area)
grid_width = len(area[0])
val_obs = 0
count_obs = 0

for obstacle in part1_nodes:
    start_col = begin_col
    direction = clockwise[0]
    visited_nodes = []
    start_row = begin_row
    empty_area = deepcopy(copy_area)
    count_obs +=1
    empty_area[obstacle[0]][obstacle[1]] = 'O'
    while start_row >= 0 and start_col >= 0 and start_row < grid_height and start_col < len(area[0]):
        if empty_area[start_row][start_col] != '#' and empty_area[start_row][start_col] != 'O':
            empty_area[start_row][start_col] = 'X'
            entry = ([start_row, start_col], direction)
            if entry not in visited_nodes:
                visited_nodes.append(([start_row, start_col], direction))
            else:
                val_obs +=1
                break
            start_row = start_row + direction[0]
            start_col = start_col + direction[1]
        else:
            start_row = start_row - direction[0]
            start_col = start_col - direction[1]
            if clockwise.index(direction) < len(clockwise) - 1:
                direction = clockwise[clockwise.index(direction) + 1]
            else:
                direction = clockwise[0]
            start_row = start_row + direction[0]
            start_col = start_col + direction[1]


print("Deel 2: " + str(val_obs))