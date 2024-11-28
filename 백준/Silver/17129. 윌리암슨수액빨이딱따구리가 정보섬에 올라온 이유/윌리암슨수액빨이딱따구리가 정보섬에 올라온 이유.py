import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

si,sj = 0,0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            si, sj = i, j

directions = [(0,-1), (-1,0), (1,0), (0,1)]

def bfs(si, sj):
    myq = deque([(si, sj, 0)])
    visited[si][sj] = 1
    while myq:
        u, v, cnt = myq.popleft()
        for i,j in directions:
            nu = u + i
            nv = v + j
            if 0 <= nu < n and 0 <= nv < m:
                if arr[nu][nv] in [3,4,5]:
                    print("TAK")
                    print(cnt+1)
                    return
                elif not visited[nu][nv] and arr[nu][nv] == 0:
                    visited[nu][nv] = 1
                    myq.append((nu, nv, cnt + 1))
    print("NIE")
    return

bfs(si, sj)