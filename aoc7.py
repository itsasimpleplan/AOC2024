with open('in7.txt') as file:
    result = []
    numbers = []
    for x in file:
        results,number = x.split(":")
        result.append(results)
        list_num = number.strip().split(" ")
        list_num = [int(item) for item in list_num]
        numbers.append(list_num)

operators = ["*", "+"]

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
                new_con = str(option) + str(num)
                options[o] = new_sum
                options.append(new_mul)
                options.append(int(new_con))
    if int(result[n]) in options:
        count = count + int(result[n])

print(count)



