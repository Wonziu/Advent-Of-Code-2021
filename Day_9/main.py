from functools import reduce

filename = "/home/wonziu/Documents/adventofcode/Day_9/input.txt"

def solve(data):
    rows = len(data)
    columns = len(data[0])    
    lows = counter = 0
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    basin = []
    mask = [[0 for __ in range(columns)] for _ in range(rows)]
    
    def wrong_coords(x, y):
        return x < 0 or x >= columns or y < 0 or y >= rows

    def wander(x, y, val):
        if (wrong_coords(x, y) or mask[y][x] == counter or data[y][x] <= val or data[y][x] == 9):
            return 0
        mask[y][x] = counter
        return 1 + sum(wander(x + dx, y + dy, data[y][x]) for dx, dy in dirs)

    for y in range(rows):
        for x in range(columns):
            if all(wrong_coords(x + dx, y + dy)
                or data[y][x] < data[y + dy][x + dx]
                for dx, dy in dirs):
                counter += 1
                basin.append(wander(x, y, -1))
                lows += data[y][x] + 1

    return lows, reduce(lambda x, y: x * y, (sorted(basin, reverse=True)[:3]))

if __name__ == '__main__':
    with open(filename) as file:
        data = [list(map(int, list(line.rstrip()))) for line in file]
        print(solve(data))
