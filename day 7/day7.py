from string import digits
from collections import defaultdict
import sys


def parse_data():
    with open(f'{sys.path[0]}/data.txt') as f:
        return f.read().splitlines()


data = parse_data()
dirs = defaultdict(int)

current_path = '/'
for i, line in enumerate(data):
    if '$ cd ' in line and '$ cd /' not in line:
        if '..' in line:
            current_path = '/'.join(current_path.split('/')[0:-1])
        else:
            new_dir = line.split(' ')[2]
            current_path = f'{current_path}/{new_dir}'
    if line[0] in digits:
        file_size = int(line.split(' ')[0])
        dirs[current_path] += file_size
        parents = current_path.split('/')
        for parent in range(1, len(parents) + 1):
            parent_path = '/'.join(current_path.split('/')[0:-parent])
            dirs[parent_path] += file_size


puzzle = 0
total_root = dirs['/']
for k, v in dirs.items():
    if v <= 100000:
        puzzle += v

print(f'Part 1: {puzzle}')

puzzle = []
needed_space = 30_000_000 - (70_000_000 - total_root)
for k, v in dirs.items():
    if v >= needed_space:
        puzzle.append(v)

print(f'Part 2: {min(puzzle)}')
