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

# create a result variable to keep track of the score
result = 0

# loop through the items in the list
for item in data:
    # get the length of the string
    length = len(item)

    # split the string into two halves
    half1 = item[:length // 2]
    half2 = item[length // 2:]

    # loop through the characters in the first half
    for char in half1:
        # check if the character is also in the second half
        if char in half2:
            # add the score to the result variable
            # a-z is 1-26 and A-Z is 27-52
            if char.islower():
                result += ord(char) - ord('a') + 1
            else:
                result += ord(char) - ord('A') + 27

            # exit the loop after the first match is found
            break

# print the final result
print(result)


