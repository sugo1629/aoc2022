import sys
import string

letters = string.ascii_uppercase
# Part 1
with open(f'{sys.path[0]}/data.txt') as f:
    data = [x for x in f.read().splitlines()]


columns = 0
for line in data:
    if ' 1   ' in line:
        columns = line.split(' ')

stacks = [[] for i in range(int(columns[-1]))]

for line in data:
    if '[' in line:
        for i, char in enumerate(line):
            if char in letters:
                stacks[int((i-1)/4)].append(char)
    if 'move' in line:
        split = line.split(' ')
        count = int(split[1])
        from_stack = int(split[3]) - 1
        to_stack = int(split[5]) - 1
        for _ in range(count):
            stacks[to_stack].insert(0, stacks[from_stack].pop(0))

puzzle = ''.join(p[0] for p in stacks)

print(f'Part 1: {puzzle}')

# Part 2
stacks = [[] for i in range(int(columns[-1]))]

for line in data:
    if '[' in line:
        for i, char in enumerate(line):
            if char in letters:
                stacks[int((i-1)/4)].append(char)
    if 'move' in line:
        split = line.split(' ')
        count = int(split[1])
        from_stack = int(split[3]) - 1
        to_stack = int(split[5]) - 1
        crates = ''
        for _ in range(0, count):
            crates = f'{crates}{stacks[from_stack][0]}'
            stacks[from_stack].pop(0)
        for i, crate in enumerate(crates):
            stacks[to_stack].insert(i, crate)

puzzle = ''.join(p[0] for p in stacks)

print(f'Part 2: {puzzle}')
