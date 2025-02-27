import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
height = [list(map(int, input().split())) for _ in range(N)]
dist = [(0, 1), (0, -1), (-1, 0), (1, 0)]
answer = 1
for h in range(1, 101):
    cnt = 0 
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] or height[i][j] <= h:
                continue
            q = deque([[i, j]])
            visited[i][j] = 1
            while q:
                now = q.popleft()
                for dx, dy in dist:
                    nx, ny = now[0]+dx, now[1]+dy
                    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and height[nx][ny] > h:
                        visited[nx][ny] = 1
                        q.append([nx, ny])
            cnt += 1
    answer = max(answer, cnt)
print(answer)
