filename = "/home/wonziu/Documents/adventofcode/Day_3/input.txt"

def binary_to_dec(l):
    return sum(int(digit) * (2 ** i) for i, digit in enumerate(l[::-1]))

def get_bits(data, f):
    count = len(data)
    res = list(map(sum, zip(*data)))
    return list(map(lambda x: 1 if f(x, count) else 0, res))

def first(data):
    gamma = get_bits(data, lambda x, count: x > count // 2)
    epsilon = list(map(lambda x: 1 - x, gamma))

    return binary_to_dec(gamma) * binary_to_dec(epsilon)

def second(data):
    bit = 0
    oxygen = co2 = data
    while (len(oxygen) > 1):
        most_common_bit = get_bits(oxygen, lambda x, count: x >= count / 2)[bit]
        oxygen = list(filter(lambda x: int(x[bit]) == most_common_bit, oxygen))
        bit += 1

    bit = 0
    while (len(co2) > 1):
        least_common_bit = get_bits(co2, lambda x, count: x < count / 2)[bit]
        co2 = list(filter(lambda x: int(x[bit]) == least_common_bit, co2))
        bit += 1    

    return binary_to_dec(oxygen[0]) * binary_to_dec(co2[0])

if __name__ == '__main__':
    with open(filename) as file:
        report = [line.rstrip('\n') for line in file]
        report = [list(map(int, line)) for line in report]
        print(first(report))
        print(second(report))
