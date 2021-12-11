from functools import reduce

filename = "input.txt"


def first(data):
    rows = len(data)
    columns = len(data[0])    
    count = 0
    dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
    basin = []
    mask = [[True for __ in range(columns)] for _ in range(rows)]

    def wrong_coords(x, y):
        return x < 0 or x >= columns or y < 0 or y >= rows

    def wander(x, y, val):
        if (wrong_coords(x, y) or not mask[y][x] or data[y][x] <= val or data[y][x] == 9):
            return 0
        mask[y][x] = False
        return 1 + sum(wander(x + dx, y + dy, data[y][x]) for dx, dy in dirs)

    for y in range(rows):
        for x in range(columns):
            if all(wrong_coords(x + dx, y + dy)
                or data[y][x] < data[y + dy][x + dx]
                for dx, dy in dirs):
                mask = [[True for __ in range(columns)] for _ in range(rows)]
                basin.append(wander(x, y, -1))
                count += data[y][x] + 1

    return count, reduce(lambda x, y: x * y, (sorted(basin, reverse=True)[:3]))

if __name__ == '__main__':
    with open(filename) as file:
        data = [list(map(int, list(line.rstrip()))) for line in file]
        print(first(data)) 