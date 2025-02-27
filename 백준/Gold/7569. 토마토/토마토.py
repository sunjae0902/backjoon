import sys
from collections import deque
input = sys.stdin.readline
M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dist = [(-1, 0, 0), (1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

# 익은 토마토는 동시에 인접한 토마토들을 익힘-> 모두 큐에 넣고 시작.
# 각 단계마다 동일하게 1씩 날짜가 증가하므로 먼저 방문한 곳이 항상 최소 값.
def bfs():
    queue = deque()
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1:  
                    queue.append((h, i, j, 0))  

    max_days = 0
    while queue:
        h, x, y, days = queue.popleft()
        max_days = max(max_days, days)
        for dh, dx, dy in dist:
            nh, nx, ny = h + dh, x + dx, y + dy
            if 0 <= nh < H and 0 <= nx < N and 0 <= ny < M and arr[nh][nx][ny] == 0:
                arr[nh][nx][ny] = 1  
                queue.append((nh, nx, ny, days + 1))  
    return max_days if all(0 not in layer for box in arr for layer in box) else -1

result = bfs()
print(result)