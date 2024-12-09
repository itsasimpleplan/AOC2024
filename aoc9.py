unpacked = []
with open('inputs/in9.txt') as file:
    for x in file:
        x = x.strip()
        y = 0
        id = 0
        while y < len(x):
            for i in range(int(x[y])):
                unpacked.append(id)
            if y < len(x) - 1:
                for j in range(int(x[y+1])):
                    unpacked.append(".")
            id = id +1
            y=y+2
y = len(unpacked)-1
moved = 0
while y >= 0:
    to_move = unpacked[y]
    if to_move != ".":
        unpacked[y] = "."
        for j in range(len(unpacked)):
            if unpacked[j] == ".":
                unpacked[j] = to_move
                break
    y = y - 1

checksum = 0
for x in range(len(unpacked)):
    if unpacked[x] != ".":
        checksum = checksum + x*unpacked[x]

print("Deel 1: " + str(checksum))