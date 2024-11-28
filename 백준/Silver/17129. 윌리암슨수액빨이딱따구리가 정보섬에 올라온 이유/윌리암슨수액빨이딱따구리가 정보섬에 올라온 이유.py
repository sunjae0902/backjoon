import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

# Find the starting position
si, sj = 0, 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            si, sj = i, j

# Directions for movement: down, up, right, left
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(si, sj):
    """Breadth-First Search to find the shortest path to a target."""
    queue = deque([(si, sj, 0)])  # (x, y, step count)
    visited[si][sj] = 1

    while queue:
        x, y, steps = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if arr[nx][ny] == 1:  # Wall
                    continue
                if arr[nx][ny] in [3, 4, 5]:  # Found target
                    return steps + 1
                visited[nx][ny] = 1
                queue.append((nx, ny, steps + 1))

    return -1  # If no path to target

# Execute BFS
result = bfs(si, sj)

if result != -1:
    print("TAK")
    print(result)
else:
    print("NIE")
