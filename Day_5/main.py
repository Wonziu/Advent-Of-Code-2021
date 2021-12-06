filename = "input.txt"

def first(data, diagonals=False):
    max_x = max_y = 0    

    for i, line in enumerate(zip(*data)):
        if i % 2 == 0:
            if max(line) > max_x:
                max_x = max(line)
        else:
            if max(line) > max_y:
                max_y = max(line)

    board = [[0 for x in range(max_x + 2)] for y in range(max_y + 2)]

    for x0, y0, x1, y1 in data:
        if diagonals or (x0 == x1 or y0 == y1):
            dx = (x1 - x0) // (max(abs(x1 - x0), 1))
            dy = (y1 - y0) // (max(abs(y1 - y0), 1))

            while x0 != x1 or y0 != y1:
                board[x0][y0] += 1
                x0 += dx
                y0 += dy
            board[x1][y1] += 1

    return sum(1 for line in board for x in line if x >= 2)

if __name__ == '__main__':
    with open(filename) as file:
        data = file.read().rstrip().split('\n')
        data = [list(map(int, entry.replace('->', '').replace(',', ' ').split())) for entry in data]
        print(first(data))
        print(first(data, True))
        