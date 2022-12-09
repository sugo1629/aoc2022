import sys


def parse_data():
    with open(f'{sys.path[0]}/data.txt') as f:
        return f.read().splitlines()


data = parse_data()
ropes = [[0, 0] for i in range(1, 11)]
t_history = set()
t9_history = set()

for line_index, line in enumerate(data):
    direction, moves = line.split(' ')
    moves = int(moves)
    # Move H
    for i in range(1, moves + 1):
        if direction == 'U':
            ropes[0][1] += 1
        if direction == 'D':
            ropes[0][1] -= 1
        if direction == 'L':
            ropes[0][0] -= 1
        if direction == 'R':
            ropes[0][0] += 1
        # Check if T needs to move
        for rope_idx, rope in enumerate(ropes):
            if rope_idx == 0:
                continue
            if abs(rope[0] - ropes[rope_idx - 1][0]) > 1 or abs(rope[1] - ropes[rope_idx - 1][1]) > 1:
                if rope[0] != ropes[rope_idx - 1][0] and rope[1] != ropes[rope_idx - 1][1]:
                    # Diagonal Move Needed
                    if rope[0] < ropes[rope_idx - 1][0]:
                        rope[0] += 1
                    if rope[0] > ropes[rope_idx - 1][0]:
                        rope[0] -= 1
                    if rope[1] < ropes[rope_idx - 1][1]:
                        rope[1] += 1
                    if rope[1] > ropes[rope_idx - 1][1]:
                        rope[1] -= 1

                elif rope[0] < ropes[rope_idx - 1][0]:
                    rope[0] += 1
                elif rope[0] > ropes[rope_idx - 1][0]:
                    rope[0] -= 1
                elif rope[1] < ropes[rope_idx - 1][1]:
                    rope[1] += 1
                elif rope[1] > ropes[rope_idx - 1][1]:
                    rope[1] -= 1
            # Log T's Position
        t_history.add(f'{ropes[1][0]},{ropes[1][1]}')
        t9_history.add(f'{ropes[9][0]},{ropes[9][1]}')

print(f'Part 1: {len(t_history)}')
print(f'Part 2: {len(t9_history)}')
