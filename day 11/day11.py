import sys
from dataclasses import dataclass
import math


@dataclass
class Monkey:
    id: int
    operation: str
    operation_value: int
    items: list
    test_divide: int
    true_monkey: int
    false_monkey: int
    total_inspect: int = 0

    def where_to_throw(self, item_worry, part1=False):
        if self.operation_value == 0:
            temp_op_value = item_worry
        else:
            temp_op_value = self.operation_value
        if self.operation == '*':
            new_worry = temp_op_value * item_worry
        elif self.operation == '+':
            new_worry = temp_op_value + item_worry
        # print(f'Item: {item_worry} in Monkey {self.id} inventory is '
        #       f'now {new_worry} ({item_worry}{self.operation}{temp_op_value})')
        if part1:
            new_worry = int(new_worry/3)
            # print(f'Item: {item_worry} in Monkey {self.id} inventory is now {new_worry} ({new_worry}/{3})')
        if new_worry % self.test_divide == 0:
            to_monkey = self.true_monkey
            if int(self.true_monkey) == 2 and int(self.id) == 0:
                print('before math:', new_worry)
                for i in range(1, 100000000):
                    if i % self.test_divide == 0 and i % 13 == 0:
                        new_worry = i
                print('after math:', new_worry)
            # if len(str(new_worry)) >= 20:
            #     new_worry = self.test_divide * 20
        else:
            to_monkey = self.false_monkey
        self.total_inspect += 1
        return [to_monkey, new_worry]

    def has_items(self):
        if len(self.items) >= 1:
            return True
        else:
            return False

    def add_item(self, item_worry):
        self.items.append(item_worry)

    def remove_items(self):
        self.items = []


def parse_data():
    with open(f'{sys.path[0]}/data.txt') as f:
        return f.read().splitlines()


def get_monkeys():
    os = ['+', '*', '/', '-']
    d = parse_data()
    m = []

    for line in d:
        if line.startswith('Monkey'):
            monkey_id = line.split(' ')[1].replace(':', '')
            continue
        if 'items' in line:
            items = [int(s) for s in line.replace(',', '').split() if s.isdigit()]
            continue
        if 'Operation' in line:
            for char in line:
                if char in os:
                    operation = char
            try:
                operation_val = [int(s) for s in line.split() if s.isdigit()][0]
            except IndexError:
                operation_val = 0
            continue
        if 'Test' in line:
            divide = [int(s) for s in line.split() if s.isdigit()][0]
            continue
        if 'true' in line:
            true_monkey = [int(s) for s in line.split() if s.isdigit()][0]
            continue
        if 'false' in line:
            false_monkey = [int(s) for s in line.split() if s.isdigit()][0]
            m.append(Monkey(monkey_id, operation, operation_val, items, divide, true_monkey, false_monkey))
    return m


monkeys = get_monkeys()

for _ in range(1, 21):
    for monkey in monkeys:
        if monkey.has_items():
            for item in monkey.items:
                to, worry = monkey.where_to_throw(item)
                print(f'Item: {worry} in Monkey {monkey.id} inventory is going to Monkey {to}')
                monkeys[to].add_item(worry)
            monkey.remove_items()
    if _ % 10 == 0:
        print(f'Round {_}')
        for m in monkeys:
            print(m.id, m.total_inspect)

puzzle = []
for m in monkeys:
    puzzle.append(m.total_inspect)
    print(m)

puzzle = sorted(puzzle, reverse=True)
print(puzzle)
print(math.prod(puzzle[:2]))

# # 85484 too low
# monkeys = get_monkeys()
#
# for _ in range(1, 10000):
#     print(_)
#     for monkey in monkeys:
#         if monkey.has_items():
#             for item in monkey.items:
#                 to, worry = monkey.where_to_throw(item)
#                 # print(f'Item: {worry} in Monkey {monkey.id} inventory is going to Monkey {to}')
#                 monkeys[to].add_item(worry)
#             monkey.remove_items()
#
# puzzle = []
# for m in monkeys:
#     puzzle.append(m.total_inspect)
#
# puzzle = sorted(puzzle, reverse=True)
# print(puzzle)
# print(math.prod(puzzle[:2]))
