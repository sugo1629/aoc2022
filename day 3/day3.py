import sys
import string

# Part 1
with open(f'{sys.path[0]}/data.txt') as f:
    data = [x for x in f.read().splitlines()]

letters = string.ascii_lowercase + string.ascii_uppercase
numbers = [i for i in range(1, 53)]
guide = dict(zip(letters, numbers))

puzzle = 0
for line in data:
    split_on = int(len(line)/2)
    first_half = line[:split_on]
    second_half = line[split_on:]

    for char in first_half:
        if char in second_half:
            puzzle += guide[char]
            break

print(f'Part 1: {puzzle}')

puzzle = 0
current_set = []
for index, line in enumerate(data, start=1):
    current_set.append(line)
    if index % 3 == 0:
        for char in current_set[0]:
            if char in current_set[1] and char in current_set[2]:
                puzzle += guide[char]
                break
        current_set = []

print(f'Part 2: {puzzle}')




