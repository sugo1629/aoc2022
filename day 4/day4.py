import sys
import string

# Part 1
with open(f'{sys.path[0]}/data.txt') as f:
    data = [x for x in f.read().splitlines()]


count = 0
for line in data:
    contained = True
    e1, e2 = line.split(',')
    e1_start, e1_end = e1.split('-')
    e2_start, e2_end = e2.split('-')
    e1_range = [i for i in range(int(e1_start), int(e1_end) + 1)]
    e2_range = [i for i in range(int(e2_start), int(e2_end) + 1)]

    if len(e1_range) < len(e2_range):
        for section in e1_range:
            if section not in e2_range:
                contained = False
    else:
        for section in e2_range:
            if section not in e1_range:
                contained = False
    if contained:
        count += 1


print(count)

# Part 2
count = 0
for line in data:
    contained = False
    e1, e2 = line.split(',')
    e1_start, e1_end = e1.split('-')
    e2_start, e2_end = e2.split('-')
    e1_range = [i for i in range(int(e1_start), int(e1_end) + 1)]
    e2_range = [i for i in range(int(e2_start), int(e2_end) + 1)]

    for section in e1_range:
        if section in e2_range:
            contained = True

    if contained:
        count += 1


print(count)
