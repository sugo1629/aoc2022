import sys

# Part 1
with open(f'{sys.path[0]}/data.txt') as f:
    data = [x for x in f.read().splitlines()]

calories = []
current_total = 0
for line in data:
    try:
        current_total += int(line)
    except ValueError:
        calories.append(current_total)
        current_total = 0

print(max(calories))

# Part 2
calories = sorted(calories, reverse=True)
print(sum(calories[:3]))
