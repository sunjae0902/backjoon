import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
answer = []
visited = [[0 for _ in range(N)] for _ in range(N)]
dist = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for i in range(N):
    for j in range(N):
        if not arr[i][j] or visited[i][j]:
            continue
        union = []
        s = deque([(i, j)])
        visited[i][j] = 1
        while s:
            now = s.popleft()
            union.append(now)
            for dx, dy in dist:
                nx, ny = now[0]+dx, now[1]+dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny]:
                    visited[nx][ny] = 1
                    s.append([nx, ny])
        answer.append(union)
answer.sort(key = lambda x: len(x))
print(len(answer))
for union in answer:
    print(len(union))
            