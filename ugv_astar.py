import heapq

# 0 = free space, 1 = obstacle
grid = [
    [0,0,0,1,0],
    [0,1,0,1,0],
    [0,0,0,0,0],
    [1,1,0,1,0],
    [0,0,0,0,0]
]

start = (0,0)
goal = (4,4)

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    pq = [(0, start)]
    visited = set()
    parent = {}

    while pq:
        cost, node = heapq.heappop(pq)

        if node == goal:
            print("Goal reached!")
            path = []
            while node in parent:
                path.append(node)
                node = parent[node]
            path.append(start)
            path.reverse()
            print("Path:", path)
            return

        if node in visited:
            continue

        visited.add(node)

        x, y = node

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_cost = cost + 1
                priority = new_cost + heuristic((nx,ny), goal)

                heapq.heappush(pq, (priority, (nx,ny)))
                parent[(nx,ny)] = node

    print("No path found")


astar(grid, start, goal)
