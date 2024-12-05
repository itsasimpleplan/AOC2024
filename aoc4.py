def search_right(row, col):
    if col+3 >= grid_width:
        return False
    else:
        if (word_search[row][col + 1] == "M"):
            if (word_search[row][col + 2] == "A"):
                if (word_search[row][col + 3] == "S"):
                    return True
    return False
def search_left(row, col):
    if col - 3 < 0:
        return False
    else:
        if (word_search[row][col - 1] == "M"):
            if (word_search[row][col - 2] == "A"):
                if (word_search[row][col - 3] == "S"):
                    return True
    return False
def search_top(row, col):
    if row - 3 < 0:
        return False
    else:
        if (word_search[row-1][col] == "M"):
            if (word_search[row-2][col] == "A"):
                if (word_search[row-3][col] == "S"):
                    return True
    return False
def search_bottom(row, col):
    if row + 3 >= grid_height:
        return False
    else:
        if (word_search[row + 1][col] == "M"):
            if (word_search[row + 2][col] == "A"):
                if (word_search[row + 3][col] == "S"):
                    return True
    return False
def search_left_top(row, col):
    if row - 3 < 0 or col -3 < 0:
        return False
    else:
        if (word_search[row - 1][col-1] == "M"):
            if (word_search[row - 2][col-2] == "A"):
                if (word_search[row - 3][col-3] == "S"):
                    return True
    return False
def search_left_bottom(row, col):
    if row + 3 >= grid_height or col -3 < 0:
        return False
    else:
        if (word_search[row + 1][col-1] == "M"):
            if (word_search[row + 2][col-2] == "A"):
                if (word_search[row + 3][col-3] == "S"):
                    return True
    return False
def search_right_bottom(row, col):
    if row + 3 >= grid_height or col + 3 >= grid_width:
        return False
    else:
        if (word_search[row + 1][col + 1] == "M"):
            if (word_search[row + 2][col + 2] == "A"):
                if (word_search[row + 3][col + 3] == "S"):
                    return True
def search_right_top(row, col):
    if row - 3 <0 or col + 3 >= grid_width:
        return False
    else:
        if (word_search[row - 1][col + 1] == "M"):
            if (word_search[row - 2][col + 2] == "A"):
                if (word_search[row - 3][col + 3] == "S"):
                    return True



with open('in4.txt') as file:
    word_search = []
    for x in file:
        x = x.strip()
        line = []
        for y in x:
            line.append(y)
        word_search.append(line)

count = 0

grid_height = len(word_search)
grid_width = len(word_search[0])

for row in range(len(word_search)):
    for col in range(len(word_search[row])):
        char = word_search[row][col]
        if(word_search[row][col] == "X"):
            if(search_right(row, col)):
                count = count +1
            if (search_left(row, col)):
                count = count + 1
            if (search_left_top(row, col)):
                count = count + 1
            if (search_left_bottom(row, col)):
                count = count + 1
            if (search_top(row, col)):
                count = count + 1
            if (search_bottom(row, col)):
                count = count + 1
            if (search_right_top(row, col)):
                count = count + 1
            if (search_right_bottom(row, col)):
                count = count + 1

print("Deel 1: "+str(count))


# --------------------- DEEL 2 ------------------------------ #
def search_left_top(row, col):
    if row - 2 < 0 or col -2 < 0:
        return False
    else:
        if (word_search[row - 1][col-1] == "A"):
            if (word_search[row - 2][col-2] == "S"):
                if (word_search[row][col-2] == "M"):
                    if (word_search[row - 1][col - 1] == "A"):
                        if (word_search[row - 2][col] == "S"):
                            return True
                if (word_search[row][col - 2] == "S"):
                    if (word_search[row - 1][col - 1] == "A"):
                        if (word_search[row - 2][col] == "M"):
                            return True
    return False
def search_left_bottom(row, col):
    if row + 3 >= grid_height or col -3 < 0:
        return False
    else:
        if (word_search[row + 1][col-1] == "M"):
            if (word_search[row + 2][col-2] == "A"):
                if (word_search[row + 3][col-3] == "S"):
                    return True
    return False
def search_right_bottom(row, col):
    if row + 2 >= grid_height or col + 2 >= grid_width:
        return False
    else:
        if (word_search[row + 1][col + 1] == "A"):
            if (word_search[row + 2][col + 2] == "S"):
                if (word_search[row][col + 2] == "S"):
                    if (word_search[row+1][col + 1] == "A"):
                        if (word_search[row + 2][col] == "M"):
                            return True
                if (word_search[row][col + 2] == "M"):
                    if (word_search[row+1][col + 1] == "A"):
                        if (word_search[row + 2][col] == "S"):
                            return True
    return False
def search_right_top(row, col):
    if row - 3 <0 or col + 3 >= grid_width:
        return False
    else:
        if (word_search[row - 1][col + 1] == "M"):
            if (word_search[row - 2][col + 2] == "A"):
                if (word_search[row - 3][col + 3] == "S"):
                    return True

count = 0
for row in range(len(word_search)):
    for col in range(len(word_search[row])):
        char = word_search[row][col]
        if(word_search[row][col] == "M"):
            if (search_left_top(row, col)):
                count = count + 1
            if (search_right_bottom(row, col)):
                count = count + 1

print("Deel 2: "+str(count))





