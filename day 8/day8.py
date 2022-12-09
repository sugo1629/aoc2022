import sys
import math

def parse_data():
    with open(f'{sys.path[0]}/data.txt') as f:
        return f.read().splitlines()


data = parse_data()
visible_trees = 0
scenic_scores = []
for line_index, tree_line in enumerate(data):
    if line_index == 0 or line_index == len(data) - 1:
        visible_trees += len(data)
        continue

    for tree_index, tree in enumerate(tree_line):
        # top, bottom, left, right.... always
        visible = [True, True, True, True]
        counter = [0, 0, 0, 0]

        if tree_index == 0 or tree_index == len(tree_line) - 1:
            visible_trees += 1
            continue
        else:
            # visible from top?
            for i in range(line_index - 1, -1, -1):
                counter[0] += 1
                if int(data[i][tree_index]) > int(tree) - 1:
                    visible[0] = False
                    break
            # visible from bottom?
            for i in range(line_index + 1, len(data)):
                counter[1] += 1
                if int(data[i][tree_index]) > int(tree) - 1:
                    visible[1] = False
                    break
            # visible from left?
            for i in range(tree_index - 1, -1, -1):
                counter[2] += 1
                if int(data[line_index][i]) >= int(tree):
                    visible[2] = False
                    break
            # visible from right?
            for i in range(tree_index + 1, len(tree_line)):
                counter[3] += 1
                if int(data[line_index][i]) >= int(tree):
                    visible[3] = False
                    break
            total_count = math.prod(counter)
            scenic_scores.append(total_count)
            if any(visible):
                # print(f'Adding Tree | Row: {line_index + 1} Tree: {tree_index + 1}')
                visible_trees += 1

print(f'Part 1: {visible_trees}')

print(f'Part 2: {max(scenic_scores)}')
