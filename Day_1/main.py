import time

from aocd.transforms import lines
filename = "/home/wonziu/Documents/adventofcode/Day_1/input.txt"

def first(lines):
    return sum(1 for i in range(1, len(lines)) if lines[i] > lines[i - 1])

def second(lines):
    sums = [sum(lines[i:i+3]) for i in range(len(lines) - 2)]
    return sum(1 for i in range(1, len(sums)) if (sums[i] > sums[i - 1]))

if __name__ == '__main__':
    with open(filename) as file:
        data = [int(line.rstrip()) for line in file]
    print(first(data))
    print(second(data))
