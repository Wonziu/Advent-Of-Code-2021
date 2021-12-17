import math

filename = "/home/wonziu/Documents/adventofcode/Day_17/input.txt"

def first(x_interval, y_interval):
    x0, x1 = x_interval
    y0, y1 = y_interval

    ys = []
    for y in range(20):
        for step in range(100):
            print("y:", y, " step:", step, " pos:", (2 * y - step + 1) * step / 2)

        # discriminant_lower = (2 * y + 1) ** 2 - 8 * y0
        # discriminant_upper = (2 * y + 1) ** 2 - 8 * y1
        # if discriminant_lower < 0 or discriminant_upper < 0:
        #     print(y, " brak")
        #     continue

        # # # numbers in between are included
        # lower_bound = [math.ceil(((2 * y + 1) - math.sqrt(discriminant_lower)) / 2), math.floor(((2 * y + 1) + math.sqrt(discriminant_lower)) / 2)]

        # # # numbers in between are excluded
        # upper_bound = [math.floor(((2 * y + 1) - math.sqrt(discriminant_upper)) / 2), math.ceil(((2 * y + 1) + math.sqrt(discriminant_upper)) / 2)]

        # left_interval = [lower_bound[0], upper_bound[0]]
        # right_interval = [upper_bound[1], lower_bound[1]]
        # ys.append((y, left_interval, right_interval))
        


if __name__ == '__main__':
    with open(filename) as file:
        _, _, x_interval, y_interval = file.read().rstrip().split()
        x_interval = list(map(int, x_interval[2:len(x_interval) - 1:].split('..')))
        y_interval = list(map(int, y_interval[2:].split('..')))
        print(first(x_interval, y_interval))