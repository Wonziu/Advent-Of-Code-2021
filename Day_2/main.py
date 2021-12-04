filename = "input.txt"

def first(data):
    depth = horizontal = 0
    for dir, val in data:
        if dir == 'up':         depth -= val
        if dir == 'down':       depth += val
        if dir == 'forward':    horizontal += val

    return (horizontal * depth)

def second(data):
    aim = depth = horizontal = 0
    for dir, val in data:
        if dir == 'up':
            aim -= val
        if dir == 'down':
            aim += val
        if dir == 'forward':
            horizontal += val
            depth += val * aim
    return (horizontal * depth)

def parse_input(line):
    dir, val = line.split()
    return (dir, int(val))

if __name__ == '__main__':
    with open(filename) as file:
        data = list(map(parse_input, file))
        print(first(data))
        print(second(data))