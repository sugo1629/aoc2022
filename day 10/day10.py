import sys


def parse_data():
    with open(f'{sys.path[0]}/data.txt') as f:
        return f.read().splitlines()


def get_sprite(location):
    sprite = [False for _ in range(0, 40)]
    for p in range(location - 1, location + 2):
        if 0 <= p <= 39:
            sprite[p] = True
    return sprite


data = parse_data()

crt = [['.' for s in range(0, 40)] for i in range(1, 7)]

x_cycles = []
x = 1

sprite_location = get_sprite(x)
for line_index, line in enumerate(data):
    if 'noop' in line:
        if sprite_location[len(x_cycles) % 40]:
            crt[int(len(x_cycles) / 40)][len(x_cycles) % 40] = '#'
        x_cycles.append(x)
        sprite_location = get_sprite(x)
    else:
        value = int(line.split(' ')[1])
        if sprite_location[len(x_cycles) % 40]:
            crt[int(len(x_cycles) / 40)][len(x_cycles) % 40] = '#'
        x_cycles.append(x)
        if sprite_location[len(x_cycles) % 40]:
            crt[int(len(x_cycles) / 40)][len(x_cycles) % 40] = '#'
        x += value
        sprite_location = get_sprite(x)
        x_cycles.append(x)


check_cycles = [20, 60, 100, 140, 180, 220]
puzzle = 0
for i, cycle in enumerate(x_cycles):
    if i + 2 in check_cycles:
        puzzle += (i + 2) * cycle

print(f'Part 1: {puzzle}')

print('Part 2:')
for line in crt:
    print(' '.join(line))
