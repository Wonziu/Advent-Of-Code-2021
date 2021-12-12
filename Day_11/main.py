filename = "input.txt"

def solve(data):
    global counter
    height = len(data)
    width = len(data[0])
    mask = [[-1 for _ in range(width)] for __ in range(height)]
    counter = step = last_counter = saved_counter = 0

    def wander(x, y):
        global counter
        if x < 0 or x >= width or y < 0 or y >= height:
            return
        if mask[y][x] != step:
            if data[y][x] == 9:
                counter += 1
                data[y][x] = 0
                mask[y][x] = step
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    wander(x + dx, y + dy)
            else:
                data[y][x] += 1

    while counter - last_counter != width * height:
        step += 1        
        last_counter = counter

        for y in range(height):
            for x in range(width):
                wander(x, y)
        if step == 100:
            saved_counter = counter

    return saved_counter, step


if __name__ == '__main__':
    with open(filename) as file:
        data = [list(map(int, line)) for line in file.read().rstrip().split('\n')]
        print(solve(data))
