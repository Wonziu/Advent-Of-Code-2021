from functools import reduce

filename = "/home/wonziu/Documents/adventofcode/Day_16/input.txt"    

# my abstract syntax tree has structure:
# operator packet: (version, typeID, sub-packets)
# literal value packet: (version, typeID, value)

def bin_to_dec(b):
    return sum((2 ** i) * digit for i, digit in enumerate(b[::-1]))

def sum_versions(ast):
    version, type_ID, rest = ast

    if type_ID == 4:
        return version

    s = sum(sum_versions(packet) for packet in rest)
    return version + s

def eval(ast):
    _, type_ID, rest = ast

    if type_ID == 4:
        return rest
    evaluated = [eval(packet) for packet in rest]
    
    match type_ID:
        case 0:
            return sum(evaluated)
        case 1:
            return reduce(lambda x, y: x * y, evaluated, 1)
        case 2:
            return min(evaluated)
        case 3:
            return max(evaluated)
        case 5:
            return 1 if evaluated[0] > evaluated[1] else 0
        case 6:
            return 1 if evaluated[0] < evaluated[1] else 0
        case 7:
            return 1 if evaluated[0] == evaluated[1] else 0

def parse(data):
    version = bin_to_dec(data[:3])
    type_ID = bin_to_dec(data[3:6])

    # operator packet   
    if type_ID != 4:
        sub_packets = []
        length_type = data[6]
        if length_type == 0:
            length = bin_to_dec(data[7:22])
            start = 22

            while length != 0:
                end, parsed = parse(data[start:])

                sub_packets.append(parsed)
                length -= end
                start += end

            return (start, (version, type_ID, sub_packets))

        if length_type == 1:
            length = bin_to_dec(data[7:18])
            start = 18
            for i in range(length):
                end, parsed = parse(data[start:])

                sub_packets.append(parsed)
                start += end
            
            return (start, (version, type_ID, sub_packets))
    
    # literal value packet
    start = 6
    value = []
    while True:
        value += data[start + 1:start + 5]
        start += 5

        if data[start - 5] == 0:
            break

    return (start, (version, type_ID, bin_to_dec(value)))

if __name__ == '__main__':
    with open(filename) as file:
        data = file.read().rstrip()
        data = [int(x) for hex in data for x in list(bin(int(hex, 16))[2:].zfill(4))]
        ast = parse(data)[1]
        print(sum_versions(ast))
        print(eval(ast))
