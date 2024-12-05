import itertools
import time

start = (round(time.time() * 1000))
with open('in51.txt') as file:
    to_check = []
    for x in file:
        line = []
        x = x.strip()
        line = x.split(",")
        to_check.append(line)

with open('in52.txt') as file:
    rules = []
    for x in file:
        x = x.strip()
        rules.append(x.split("|"))
sum_middle = 0
def check_list(list, rules_check):
    for y in rules_check:
        if list.index(y[1]) < list.index(y[0]):
            return False, rules_check.index(y)
    return True, 0

def check_list_rec(list, rules_check):
    for y in rules_check:
        if list.index(y[1]) < list.index(y[0]):
            return False, y
    return True, -1


def rel_rules(list):
    relevant_rules = []
    for y in rules:
        if y[0] in list and y[1] in list:
            relevant_rules.append(y)
    return relevant_rules


failed_updates = []
reli_rules = []
idxs = []
for x in to_check:
    correct, idx = check_list(x, rel_rules(x))
    if correct:
        sum_middle = sum_middle + int(x[int((len(x) - 1)/2)])
    else:
        failed_updates.append(x)
        reli_rules.append(rel_rules(x))
        idxs.append(idx)



sum_middle = 0
for x in range(len((failed_updates))):
    check, idx = check_list_rec(failed_updates[x], reli_rules[x])
    while not check:
        #print(type(idx))
        if (type(idx) == list):
            failed_updates[x].remove(idx[0])
            index = failed_updates[x].index(idx[1])
            failed_updates[x].insert(index, idx[0])
        check, idx = check_list_rec(failed_updates[x], reli_rules[x])
        if(check):
            sum_middle = sum_middle + int(failed_updates[x][int((len(failed_updates[x]) - 1) / 2)])
now = round(time.time() * 1000)
print(now-start)
print(sum_middle)

