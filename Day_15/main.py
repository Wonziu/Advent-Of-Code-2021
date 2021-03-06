import heapq

filename = "/home/wonziu/Documents/adventofcode/Day_15/input.txt"

def dijkstra(board, depth):
    height = len(board)
    width = len(board[0])
    
    queue = [(0, (0, 0))]
    dist = [[float('inf') for x in range(width * depth)] for y in range(height * depth)]
    dist[0][0] = 0

    while queue:
        distance, node = heapq.heappop(queue)        
        if node == (height * depth - 1, width * depth - 1):
            break

        for dir in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = node
            dx, dy = dir
            new_x = x + dx
            new_y = y + dy

            # we are never gonna have relaxation since edges have weight = 0
            if width * depth > new_x >= 0 and height * depth > new_y >= 0:
                if dist[new_x][new_y] == float('inf'):
                    neigh_distance = distance + (board[new_x % width][new_y % height] + 
                        new_x // width + new_y // height - 1) % 9 + 1

                    dist[new_x][new_y] = neigh_distance
                    heapq.heappush(queue, (neigh_distance, (new_x, new_y)))

    return dist[height * depth - 1][width * depth - 1]

if __name__ == '__main__':
    with open(filename) as file:
        data = file.read().rstrip().split()
        data = [list(map(int, list(line))) for line in data]
        
        print(dijkstra(data, 1))
        print(dijkstra(data, 5))
