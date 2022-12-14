import sys


def tuner(unique_count, input_data):
    chars = set()
    for i, char in enumerate(input_data[0]):
        chars.add(char)
        for c in range(i + 1, i + unique_count):
            try:
                chars.add(input_data[0][c])
            except IndexError:
                return 0
        if len(chars) == unique_count:
            return i + unique_count
        chars = set()
    return 0


with open(f'{sys.path[0]}/data.txt') as f:
    data = [x for x in f.read().splitlines()]

print(f'Part 1: {tuner(4, data)}')
print(f'Part 2: {tuner(14, data)}')
