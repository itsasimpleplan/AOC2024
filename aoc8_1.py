import itertools

with open('in8.txt') as file:
    area = []
    for x in file:
        x = x.strip()
        line = []
        for y in x:
            line.append(y)
        area.append(line)
unique_letters = []

grid_height = len(area)
grid_width = len(area[0])

for x in area:
    for y in x:
        if y not in unique_letters and y != '.':
            unique_letters.append(y)
        #unique_letters.append(list(set(y)))


location_letters = []

for l in unique_letters:
    list_loca = []
    for x in range(len(area)):
        for y in range(len(area[x])):
            if(area[x][y]==l):
                list_loca.append((x,y))
    location_letters.append(list_loca)
antinodes = []
for i in location_letters:
    for pair in itertools.combinations(i,2):
        ya = pair[0][0]-pair[1][0]
        yb = pair[0][1]-pair[1][1]

        antinode1 = (pair[0][0] + ya, pair[0][1] + yb)
        antinode2 = (pair[0][0] - ya, pair[0][1] - yb)
        antinode3 = (pair[1][0] + ya, pair[1][1] + yb)
        antinode4 = (pair[1][0] - ya, pair[1][1] - yb)

        if antinode1[0] >= 0 and antinode1[0]  <grid_height and antinode1 != pair[0] and antinode1 != pair[1]:
                if antinode1[1] >= 0 and antinode1[1] < grid_width:
                    if antinode1 not in antinodes:
                        antinodes.append(antinode1)

        if antinode2[0] >= 0 and antinode2[0] <grid_height  and antinode2 != pair[0] and antinode2 != pair[1]:
                if antinode2[1] >= 0 and antinode2[1] < grid_width:
                    if antinode2 not in antinodes:
                        antinodes.append(antinode2)
        if antinode3[0] >= 0 and antinode3[0] < grid_height  and antinode3 != pair[0] and antinode3 != pair[1]:
                if antinode3[1] >= 0 and antinode3[1] < grid_width:
                    if antinode3 not in antinodes:
                        antinodes.append(antinode3)
        if antinode4[0] >= 0 and antinode4[0] < grid_height  and antinode4 != pair[0] and antinode4 != pair[1]:
                if antinode4[1] >= 0 and antinode4[1] < grid_width:
                    if antinode4 not in antinodes:
                        antinodes.append(antinode4)


print("Deel 1: " + str(len((antinodes))))