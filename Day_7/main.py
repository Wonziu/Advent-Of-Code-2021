import statistics
import math

filename = "/home/wonziu/Documents/adventofcode/Day_7/input.txt"

def first(data):
    align = round(statistics.median(data))
    return sum(abs(align - x) for x in data)

def triangular_distance(x, y):
    return int(abs(x - y) * (1 + abs(x - y)) / 2)

def second(data):
    align = statistics.mean(data)
    lower = int(math.floor(align))
    upper = int(math.ceil(align))
    return min(sum(triangular_distance(lower, x) for x in data), sum(triangular_distance(upper, x) for x in data))

if __name__ == '__main__':
    with open(filename) as file:
        data = list(map(int, file.read().rstrip().split(',')))
        print(first(data))
        print(second(data))
