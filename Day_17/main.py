import math

filename = "/home/wonziu/Documents/adventofcode/Day_17/input.txt"

def first(x_interval, y_interval):
    # Because we are always gonna land on point (x, 0) with velocity (_, -y - 1) so for
    # y = abs(y0 + 1) we're always gonna overshoot
    greatest_y = abs(y_interval[0] + 1)    
    # highest is gonna be the value of arithmetic sum of a sequence y_n = y - n + 1 from 1 to y
    highest_y = (greatest_y + 1) * greatest_y // 2
    return highest_y

def second(x_interval, y_interval):
    y0, y1 = y_interval
    x0, x1 = x_interval

    greatest_y = abs(y_interval[0] + 1)
    smallest_y = y_interval[0]
    ys = []
    for y in range(smallest_y, greatest_y + 1):
        discriminant_lower = (2 * y + 1) ** 2 - 8 * y0
        discriminant_upper = (2 * y + 1) ** 2 - 8 * y1
        if discriminant_lower < 0:
            continue

        # numbers in between are included
        lower_bound = [math.ceil(((2 * y + 1) - math.sqrt(discriminant_lower)) / 2), math.floor(((2 * y + 1) + math.sqrt(discriminant_lower)) / 2)]


        if discriminant_upper != 0:
            # numbers in between are excluded
            upper_bound = [math.floor(((2 * y + 1) - math.sqrt(discriminant_upper)) / 2), math.ceil(((2 * y + 1) + math.sqrt(discriminant_upper)) / 2)]
        else:
            # case when our parabola is above the x-axis. Almost impossible
            upper_bound = [-1000, 1000]

        # some shenanigans to get nice intervals
        if lower_bound[1] >= 0 and upper_bound[1] <= lower_bound[1]:
            right_interval = [max(0, upper_bound[1]), lower_bound[1]]
            ys.append((y, right_interval))

        if upper_bound[0] >= lower_bound[0] and upper_bound[0] >= 0:
            left_interval = [max(0, lower_bound[0]), upper_bound[0]]
            ys.append((y, left_interval))


    greatest_x = x_interval[1]
    # for smallest_x we have to find smallest n that the sum of an arithmetic sequence x = x - n + 1 is >= x0
    smallest_x = 0
    discriminant = 1 + 8 * x0
    if discriminant >= 0:
        smallest_x = max(0, math.ceil((-1 + math.sqrt(discriminant)) / 2))

    velocities = set()
    for y, [a, b] in ys:
        for x in range(smallest_x, greatest_x + 1):
            for step in range(a, b + 1):
                x_pos = 0
                
                if step >= x:
                    x_pos = (x + 1) * x / 2
                else:
                    x_pos = (2 * x - step + 1) * step / 2

                if x0 <= x_pos <= x1:
                    velocities.add((x, y))

    return len(velocities)

if __name__ == '__main__':
    with open(filename) as file:
        _, _, x_interval, y_interval = file.read().rstrip().split()
        x_interval = list(map(int, x_interval[2:len(x_interval) - 1:].split('..')))
        y_interval = list(map(int, y_interval[2:].split('..')))
        print(first(x_interval, y_interval))
        print(second(x_interval, y_interval))