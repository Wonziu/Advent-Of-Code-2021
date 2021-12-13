filename = "/home/wonziu/Documents/adventofcode/Day_13/input.txt"

def print_board(points):
    width = max(point[0] for point in points) + 1
    height = max(point[1] for point in points) + 1
    for y in range(height):
        for x in range(width):
            if (x, y) in points:
                print("#", end="")
            else:
                print("-", end="")
        print()

def solve(points, folds):
    for axis, eq in folds:
        folded = set()

        for point in points:
            x = min(point[0], 2 * eq - point[0]) if axis == 'x' else point[0]
            y = min(point[1], 2 * eq - point[1]) if axis == 'y' else point[1]
            folded.add((x, y))

        points = folded
    return points

if __name__ == '__main__':
    with open(filename) as file:
        points, folds = file.read().rstrip().split('\n\n')
        points = set([(int(coord.split(',')[0]), int(coord.split(',')[1])) for coord in points.split('\n')])
        folds = [[fold[11], int(fold[13:])] for fold in folds.split('\n')]
        sol_1 = solve(points, folds[:1])
        print(len(sol_1))
        sol_2 = solve(points, folds)
        print_board(sol_2)
