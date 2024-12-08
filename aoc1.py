l1 = []
l2 = []
with open('inputs/in1.txt') as file:
    for x in file:
        x = x.strip()
        x = x.split(" ")
        l1.append(int(x[0]))
        l2.append(int(x[-1]))

l1.sort()

l2.sort()
diff = []
while l1 != []:
    m1 = l1.pop(0)
    m2 = l2.pop(0)

    diff.append(abs(m1 - m2))

print("Deel 1: "+str(sum(diff)))

with open('inputs/in1.txt') as file:
    for x in file:
        x = x.strip()
        x = x.split(" ")
        l1.append(int(x[0]))
        l2.append(int(x[-1]))

sum = 0
for x in l1:
    sum = sum + (x*l2.count(x))

print("Deel 1: "+str(sum))

