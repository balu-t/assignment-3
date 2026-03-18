import heapq

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def astar(grid, start, goal):
    pq = [(0, start)]
    visited = set()

    while pq:
        cost, node = heapq.heappop(pq)

        if node == goal:
            print("Reached goal")
            return True

        if node in visited:
            continue

        visited.add(node)

        x, y = node

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x+dx, y+dy

            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == 0:
                    priority = cost + 1 + heuristic((nx,ny), goal)
                    heapq.heappush(pq, (priority, (nx,ny)))

    return False


# Dynamic environment
grid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]

start = (0,0)
goal = (2,2)

print("Initial path search:")
astar(grid, start, goal)

# Suddenly obstacle appears
grid[1][0] = 1

print("\nAfter obstacle change:")
astar(grid, start, goal)
