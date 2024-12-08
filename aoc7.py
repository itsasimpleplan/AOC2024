with open('in7.txt') as file:
    result = []
    numbers = []
    for x in file:
        results,number = x.split(":")
        result.append(results)
        list_num = number.strip().split(" ")
        list_num = [int(item) for item in list_num]
        numbers.append(list_num)

count = 0

for n in range(len(numbers)):
    options = []
    for num in numbers[n]:
        if options == []:
            options.append(num)
        else:
            for o in range(len(options)):
                option = options[o]
                new_sum = option + num
                new_mul = option * num
                # commend out this next line for part 1
                new_con = str(option) + str(num)
                options[o] = new_sum
                options.append(new_mul)
                # commend out this next line for part 1
                options.append(int(new_con))
    if int(result[n]) in options:
        count = count + int(result[n])

#print("Deel 1: " + str(count))
print("Deel 2: " + str(count))



