filename = "/home/wonziu/Documents/adventofcode/Day_17/additional_input.txt"

if __name__ == '__main__':
    with open(filename) as file:
        data = file.read().rstrip().split()
        data = [line.split(',') for line in data]
        data = sorted(data, key=lambda x: int(x[1]))
        for x, y in data:
            print(x, y)