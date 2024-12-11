with open('inputs/in10.txt') as file:
    area = []
    for x in file:
        x = x.strip()
        line = []
        for y in x:
            if y.isnumeric():
                line.append(int(y))
            else:
                line.append(y)
        area.append(line)
starting_points = []
for x in range(len(area)):
    for y in range(len(area[x])):
        if area[x][y] == 0:
            starting_points.append((x,y))

grid_height = len(area)
grid_width = len(area[0])

def search_right(row, col, num):
    if col +1 >= grid_width:
        return False
    else:
        if (area[row][col + 1] == num+1):
            return True
    return False
def search_left(row, col, num):
    if col - 1 < 0:
        return False
    else:
        if (area[row][col - 1] == num+1):
            return True
    return False
def search_top(row, col,num):
    if row - 1 < 0:
        return False
    else:
        if (area[row-1][col] == num+1):
                    return True
    return False
def search_bottom(row, col,num):
    if row + 1 >= grid_height or num == ".":
        return False
    else:
        test = area[row + 1][col]
        if (area[row + 1][col] == num+1):
            return True
checksum = 0
checktrail = 0
for x in starting_points:
    options = []
    options.append(x)
    count = 0
    for y in options:
        if search_top(y[0],y[1],area[y[0]][y[1]]):
            options.append((y[0]-1,y[1]))
        if search_bottom(y[0], y[1], area[y[0]][y[1]]):
            options.append((y[0] + 1, y[1]))
        if search_left(y[0], y[1], area[y[0]][y[1]]):
            options.append((y[0], y[1]-1))
        if search_right(y[0], y[1], area[y[0]][y[1]]):
            options.append((y[0], y[1]+1))
    score_set = set(options)
    for x in score_set:
        if area[x[0]][x[1]] == 9:
            count = count+1
    checksum = checksum + count
    trail_length = 0
    for x in options:
        if area[x[0]][x[1]] == 9:
            trail_length = trail_length + 1
    checktrail = checktrail + trail_length

print("Deel 1: "+ str(checksum))
print("Deel 2: "+ str(checktrail))

