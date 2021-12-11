filename = "input.txt"

def first(data):
    rows = len(data)
    columns = len(data[0])    
    count = 0

    for y in range(rows):
        for x in range(columns):
            if all(dx + x < 0 
                or dx + x >= columns 
                or dy + y < 0 
                or dy + y >= rows 
                or data[y][x] < data[y + dy][x + dx]
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0))):
                count += data[y][x] + 1
    return count

if __name__ == '__main__':
    with open(filename) as file:
        data = [list(map(int, list(line.rstrip()))) for line in file]
        print(first(data))  