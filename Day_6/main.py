filename = "input.txt"

def first(data):
    fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    for x in data:
        fish[x] += 1

    for day in range(256):
        new_fish = fish[0]
        fish[0:8] = fish[1:9]
        fish[8] = new_fish
        fish[6] += new_fish 
    return sum(fish)

if __name__ == '__main__':
    with open(filename) as file:
        data = list(map(int, file.read().split(',')))
        print(first(data))