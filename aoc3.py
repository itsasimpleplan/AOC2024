import ast
import re


with open('in3.txt') as file:
    for x in file:
        txt=x
        txt2= x

instructions = re.findall("mul\(\d{1,3},\d{1,3}\)", txt)
instructions = [ast.literal_eval(sub[3:]) for sub in instructions]
sum = 0
for i in instructions:
    sum = sum + (i[0]*i[1])

print(sum)

x1 = re.findall("mul\(\d{1,3},\d{1,3}\)", txt)
x2 = re.split("mul\(\d{1,3},\d{1,3}\)", txt2)

print(x1)
print(x2)

valid = []
val = True


for x in range(len(x2) - 1):
    test = x2[x]
    test2 = x1[x]
    if(val):
        if re.search("don't\(\)", x2[x]) == None:
            valid.append(x1[x])
        else:
            val = False
    if not val:
        if re.search("do\(\)", x2[x]) != None:
            val = True
            valid.append(x1[x])


print(valid)

instructions = [ast.literal_eval(sub[3:]) for sub in valid]
sum = 0
for i in instructions:
    sum = sum + (i[0]*i[1])

print(sum)