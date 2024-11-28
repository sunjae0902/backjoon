import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
sarr = []
flag = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            flag = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            sarr.append((i, j))
def bfs(sarr):
    directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    q = deque()
    for si, sj in sarr:
        q.append((si, sj, 0))
        visited[si][sj] = 1
    if not q:
        return -1
    while q:
        x, y, days = q.popleft()
        for i,j in directions:
            nx, ny = x + i, y + j
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and not arr[nx][ny]:
                    visited[nx][ny] = 1
                    arr[nx][ny] = 1
                    q.append((nx, ny, days + 1))  
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                return -1
    return days      
        

if not flag:
    print(0)
else:
    cnt = bfs(sarr)
    print(cnt)