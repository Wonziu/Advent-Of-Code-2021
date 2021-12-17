from operator import add

filename = "/home/wonziu/Documents/adventofcode/Day_14/input.txt"

# solution uses DP
#             ╓───────────────────────────────╥─────────────────────────────
# step:       ║               0               ║               1         ...
#             ╟───────┬───────┬───────┬───────╫───────┬───────┬───────┬─────
# pair:       ║  AA   │  AB   │  BA   │  BB   ║  AA   │  AB   │  BA   │ ...
#             ╟───┬───┼───┬───┼───┬───┼───┬───╫───┬───┼───┬───┼───┬───┼───┬─
# character:  ║ A │ B │ A │ B │ A │ B │ A │ B ║ A │ B │ A │ B │ A │ B │ ...
#             ╠═══╪═══╪═══╪═══╪═══╪═══╪═══╪═══╬═══╪═══╪═══╪═══╪═══╪═══╪═══╪═
# count:      ║ 2 │ 0 │ 1 │ 1 │ 1 │ 1 │ 0 │ 2 ║ 3 │ 0 │ 2 │ 1 │ 2 │ 1 │ ...
#             ╙───┴───┴───┴───┴───┴───┴───┴───╨───┴───┴───┴───┴───┴───┴───┴─
# products: AA -> AAA, AB -> AAB, BA -> BAA, ...
# I'm using some optimization so that i only need two rows of my dp
# dp[i][j][k][l] = dp[steps][first letter][second letter][frequency of a letter]
# dp[i][j][k] = dp[i - 1][j][x] + dp[i - 1][x][k] and we have to substract 1 at the index of x
# assuming that we have a product jk -> jxk

def solve(template, rules, depth):
    letter_to_num = {}
    size = 0

    for key, value in rules.items():
        for i in range(2):
            if key[i] not in letter_to_num:                
                letter_to_num[key[i]] = size
                size += 1
    num_to_letter = {v: k for k, v in letter_to_num.items()}

    dp = [[[[2 if l == k == j else 1 if l == k or l == j else 0 for l in range(size)] 
        for k in range(size)] for j in range(size)] for i in range(2)]
    
    for step in range(1, depth + 1):
        for j in range(size):
            for k in range(size):
                    a = num_to_letter[j]
                    b = num_to_letter[k]
                    product = letter_to_num[rules[a + b]]
                    dp[step % 2][j][k] = list(map(add, dp[(step + 1) % 2][j][product], dp[(step + 1) % 2][product][k]))
                    dp[step % 2][j][k][product] -= 1

    result = [0] * size
    for i in range(len(template) - 1):
        a = letter_to_num[template[i]]
        b = letter_to_num[template[i+1]]
        result = list(map(add, result, dp[depth % 2][a][b]))

    for i in range(1, len(template) - 1):
        result[letter_to_num[template[i]]] -= 1

    return sorted(result)[-1] - sorted(result)[0]

if __name__ == '__main__':
    with open(filename) as file:
        template, rules = file.read().rstrip().split('\n\n')

        rules = [line.split(' -> ') for line in rules.split('\n')]
        items = {}
        for rule in rules:
            key, value = rule
            items[key] = value

        print(solve(template, items, 10))
        print(solve(template, items, 40))
