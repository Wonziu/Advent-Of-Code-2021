import math

filename = "/home/wonziu/Documents/adventofcode/Day_17/input.txt"

def first(x_interval, y_interval):
    # Because we are always gonna land on point (x, 0) with velocity (_, -y - 1) so for
    # y = abs(y0 + 1) we're always gonna overshoot
    greatest_y = abs(y_interval[0] + 1)    
    # highest is gonna be the value of arithmetic sum of a sequence y_n = y - n + 1 from 1 to y
    highest_y = (greatest_y + 1) * greatest_y // 2
    return highest_y


if __name__ == '__main__':
    with open(filename) as file:
        _, _, x_interval, y_interval = file.read().rstrip().split()
        x_interval = list(map(int, x_interval[2:len(x_interval) - 1:].split('..')))
        y_interval = list(map(int, y_interval[2:].split('..')))
        print(first(x_interval, y_interval))