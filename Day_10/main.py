from functools import reduce

filename = "/home/wonziu/Documents/adventofcode/Day_10/input.txt"

def solve(data):
    points_first = 0
    points_second = []
    score_first = { ')' : 3, ']' : 57, '}' : 1197, '>' : 25137 }
    score_second = { ')' : 1, ']' : 2, '}' : 3, '>' : 4 }
    closing = { '(' : ')', '[' : ']', '{' : '}', '<' : '>' }

    for line in data:
        stack = []
        corrupted = False
        for x in line:
            if x in ['(', '[', '{', '<']:
                stack.append(x)
            else:
                if closing[stack.pop()] != x:
                    points_first += score_first[x]
                    corrupted = True
        
        if not corrupted:
            points_second.append(reduce(lambda x, y: x * 5 + y, map(lambda x: score_second[closing[x]], stack[::-1])))
    return points_first, sorted(points_second)[len(points_second) // 2]

if __name__ == '__main__':
    with open(filename) as file:
        data = file.read().rstrip().split('\n')
        print(solve(data))
