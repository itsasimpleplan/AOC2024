import itertools

with open('inputs/in8.txt') as file:
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

        x = pair[0][0] + ya
        y =  pair[0][1] + yb

        while x >= 0 and x < grid_height and y >=0 and y <grid_width:
            antinodes.append((x,y))
            x = x + ya
            y = y + yb
        x = pair[0][0] - ya
        y = pair[0][1] - yb
        while x >= 0 and x < grid_height and y >=0 and y <grid_width:
            antinodes.append((x,y))
            x = x - ya
            y = y - yb
        x = pair[1][0] + ya
        y = pair[1][1] + yb
        while x >= 0 and x < grid_height and y >=0 and y <grid_width:
            antinodes.append((x,y))
            x = x + ya
            y = y + yb
        x = pair[1][0] - ya
        y = pair[1][1] - yb
        while x >= 0 and x < grid_height and y >= 0 and y < grid_width:
            antinodes.append((x, y))
            x = x - ya
            y = y - yb

antinodes = list(set(antinodes))
print("Deel 2: " + str(len((antinodes))))