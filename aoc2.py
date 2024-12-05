safe = 0


def gen_perm(list):
    list_list = []
    for y in range(len(list)):
        new_list = []
        for x in range(len(list)):
            if(y != x):
                new_list.append(list[x])
        list_list.append(new_list)
    return list_list


def check_safe(to_check_report):
    dec = 0
    inc = 0
    for level in range(len(to_check_report) - 1):
        diff = int(to_check_report[level]) - int(to_check_report[level + 1])
        if diff > 0 and diff < 4:
            dec = dec + 1
        if diff < 0 and diff > -4:
            inc = inc + 1
    if dec == len(to_check_report) - 1:
        return True
    if inc == len(to_check_report) - 1:
        return True


with open('in2.txt') as file:
    for x in file:
        x = x.strip()
        report = x.split()
        opt_rem = gen_perm(report)
        safe_rep = 0
        for check_rep in opt_rem:
            if check_safe(check_rep):
                safe_rep = safe_rep + 1
        full_check = check_safe(report)
        if safe_rep > 0 or full_check:
            safe = safe +1


print(safe)



