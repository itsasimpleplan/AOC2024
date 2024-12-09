unpacked = []
numbers = []
with open('inputs/in9.txt') as file:
    for x in file:
        input = list(x.strip())

with open('inputs/in9.txt') as file:
    for x in file:
        x = x.strip()
        y = 0
        id = 0
        while y < len(x):
            numbers.append(id)
            if y < len(x)-1:
                numbers.append(".")
            id = id +1
            y=y+2


y = len(input)-1
checked = []
while y >=0:
    to_move = numbers[y]
    if(to_move not in checked and to_move != "."):
        checked.append(to_move)
        amount_to_move = int(input[y])
        for x in range(len(input)):
            space_to_check = numbers[x]
            if space_to_check == to_move:
                break
            if space_to_check == ".":
                amount_to_check = int(input[x])
                if amount_to_check >= amount_to_move:
                        extra = amount_to_check - amount_to_move
                        if extra == 0:
                            numbers[x] = to_move
                            input[x] = amount_to_move
                            numbers[y] = "."
                            input[y] = amount_to_move
                            break
                        else:
                            numbers.insert(x, to_move)
                            input[x] = extra
                            input.insert(x, amount_to_move)
                            numbers[y+1] = "."
                            break
        y = y-1
    else:
        y = y -1

checksum = 0
id = 0
for x in range(len(numbers)):
    if(numbers[x] != "."):
        for y in range((int(input[x]))):
            checksum = checksum + int(numbers[x])*id
            id = id + 1
    else:
        id = id + int(input[x])

print("Deel 2: " + str(checksum))