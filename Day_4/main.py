filename = "/home/wonziu/Documents/adventofcode/Day_4/input.txt"

def check_row(bingo):
    return any(sum(row) == -5 for row in bingo)

def check_col(bingo):
    return any(sum(column) == -5 for column in zip(*bingo))

def replace(list, el, new):
    for line in list:
        for i in range(len(line)):
            if line[i] == el:
                line[i] = new

def first(data, input):
    for x in input:
        for bingo in data:
            replace(bingo, x, -1)
            if check_row(bingo) or check_col(bingo):
                replace(bingo, -1, 0)
                return x * sum(map(sum, bingo))
                        
def second(data, input):
    max = len(data)
    counter = 0
    mask = [1] * max

    for x in input:
        for i, bingo in enumerate(data):
            if mask[i] == 1:
                replace(bingo, x, -1)
                if check_row(bingo) or check_col(bingo):
                    counter += 1
                    mask[i] = 0
                    if counter == max:
                        replace(bingo, -1, 0)
                        return x * sum(map(sum, bingo))

if __name__ == '__main__':
    with open(filename) as file:
        numbers, *boards = file.read().rstrip().split('\n\n')
        input = [int(num) for num in numbers.split(',')]
        boards = [board.split() for board in boards]
        bingos = [[list(map(int, board[i:i+5])) for i in range(0, len(board), 5)] for board in boards]
        
        print(first(bingos, input))
        print(second(bingos, input))
