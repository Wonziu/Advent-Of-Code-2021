filename = "/home/wonziu/Documents/adventofcode/Day_8/input.txt"

def get_number(mask):
    if mask == 119: 
        return 0 
    if mask == 18:
        return 1
    if mask ==  93: 
        return 2
    if mask == 91: 
        return 3
    if mask == 58:
        return 4
    if mask == 107: 
        return 5
    if mask == 111:
        return 6
    if mask == 82:
        return 7
    if mask == 127:
        return 8
    if mask == 123:
        return 9
    return -1

def get_perms(elements):
    length = len(elements)
    if length <= 1:
        yield elements
    else:
        for perm in get_perms(elements[1:]):
            for i in range(length):
                yield perm[:i] + elements[0:1] + perm[i:]

def second(inputs, outputs):
    bits = [64, 32, 16, 8, 4, 2, 1]
    sum = 0

    for input, output in zip(inputs, outputs):
        for perm in get_perms(bits):
            correct_perm = True
            
            for entry in input:
                mask = 0
                for letter in entry:
                    mask += perm[ord(letter) - ord('a')]
                if (get_number(mask) == -1):
                    correct_perm = False
                    break

            if correct_perm:
                i = len(output) - 1
                for entry in output:
                    mask = 0
                    for letter in entry:
                        mask += perm[ord(letter) - ord('a')]
                    sum += get_number(mask) * (10 ** i)
                    i -= 1
                break

    return sum

def first(data):
    return sum(1 for line in data for x in line if len(x) == 2 or len(x) == 4 or len(x) == 3 or len(x) == 7)
     

if __name__ == '__main__':
    with open(filename) as file:
        data = file.read().rstrip().split('\n')
        o = [line.split('|')[1].split() for line in data]
        i = [line.split('|')[0].split() for line in data]
        print(first(o))
        print(second(i, o))
