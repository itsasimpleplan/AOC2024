from copy import deepcopy

with open('inputs/in11.txt') as file:
    for stones in file:
        stones = stones.strip()
        stones = stones.split()

        stones = [int(x) for x in stones]

dict = {}
for s in stones:
    dict[s] = 1


s = 0
stop = len(dict)


def get_id(num):
    for x in range(len(dict)):
        if dict[x][0] == num:
            return x
    return -1

def count_stones(dict):
    sum = 0
    for x in dict:
        sum = sum + x[1]
    return sum

blinks = 75

for blink in range(blinks):
    stop = len(dict)
    new_stones = {}
    keys = dict.keys()
    for stone in keys:
        if stone == 0:
            if 1 in new_stones.keys():
                val = new_stones[1]
                new_stones[1] = val+dict[stone]
            else:
                new_stones[1] = dict[stone]

        elif len(str(stone)) % 2 == 0:
            stone_string = str(stone)
            # stone_string = str(stones[s])
            length_stone = int(len(stone_string)/2)
            first_stone = int(stone_string[:length_stone])
            second_stone = int(stone_string[length_stone:])

            if first_stone in new_stones.keys():
                old_val = new_stones[first_stone]
                new_stones[first_stone] = old_val + dict[stone]
            else:
                new_stones[first_stone] = dict[stone]

            if second_stone in new_stones:
                old_val = new_stones[second_stone]
                new_stones[second_stone] = old_val + dict[stone]
            else:
                new_stones[second_stone] = dict[stone]
        else:
            new_val = stone*2024
            if new_val in  new_stones.keys():
                old_val = new_stones[new_val]
                new_stones[new_val] = old_val + dict[stone]
            else:
                new_stones[new_val] = dict[stone]

    dict = deepcopy(new_stones)

print("Outcome: "+ str(sum(new_stones.values())))