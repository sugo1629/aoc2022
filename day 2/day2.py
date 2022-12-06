import sys

# Part 1
with open(f'{sys.path[0]}/data.txt') as f:
    data = [x for x in f.read().splitlines()]

print(data)
score_rules = {'A': 1, 'X': 1,
               'B': 2, 'Y': 2,
               'C': 3, 'Z': 3}

total_score = 0
for d in data:
    round_score = 0
    o, y = d.split(" ")
    elf = score_rules[o]
    you = score_rules[y]

    if elf == you:
        total_score += you + 3
    elif elf == 1 and you == 2:
        total_score += you + 6
    elif elf == 2 and you == 3:
        total_score += you + 6
    elif elf == 3 and you == 1:
        total_score += you + 6
    else:
        total_score += you

print(f'Part 1: {total_score}')

# Part 2
total_score = 0
for d in data:
    round_score = 0
    e, y = d.split(" ")
    elf = score_rules[e]
    you = score_rules[y]

    if you == 1:
        if elf == 1:
            total_score += 3
        elif elf == 2:
            total_score += 1
        elif elf == 3:
            total_score += 2
    elif you == 2:
        total_score += elf + 3
    elif you == 3:
        if elf == 1:
            total_score += 8
        elif elf == 2:
            total_score += 9
        elif elf == 3:
            total_score += 7

print(f'Part 2: {total_score}')
