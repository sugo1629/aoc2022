import sys


def parse_data():
    with open(f'{sys.path[0]}/data.txt') as f:
        return f.read().splitlines()


data = parse_data()
