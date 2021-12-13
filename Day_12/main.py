filename = "/home/wonziu/Documents/adventofcode/Day_12/input.txt"

edges = {}

def first(node, visited):
    if node == 'end':
        return 1

    if node.islower():
        visited.append(node)

    neighbours = edges[node]
    return sum(first(n, [*visited]) for n in neighbours if n.isupper() or n not in visited)

def second(node, visited, no_duplicates):
    if node == 'end':
        return 1

    if node.islower():
        if node in visited:
            no_duplicates = False
        else:
            visited.append(node)

    neighbours = edges[node]
    return sum(second(n, [*visited], no_duplicates) for n in neighbours if n != 'start' and (n.isupper() or n not in visited or no_duplicates))


if __name__ == '__main__':
    with open(filename) as file:
        data = file.read().rstrip().split('\n')
        data = [line.split('-') for line in data]
        
        for a, b in data:
            for _ in range(2):
                if edges.get(a, False):
                    edges[a].append(b)
                else:
                    edges[a] = [b]
                a, b = b, a

        print(first('start', []))
        print(second('start', [], True))
