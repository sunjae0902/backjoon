import sys
from collections import deque
input = sys.stdin.readline

N,K = map(int, input().split())
visited = [0] * (1000001)

def bfs(s):
    q = deque([(s, 0)])
    visited[s] = 1
    while q:
        x, cnt = q.popleft()
        dist = [1, -1, x]
        for d in dist:
            nx = x + d
            if 0 <= nx <= 1000000 and not visited[nx]:
                if nx == K:
                    print(cnt+1)
                    return
                else:
                    visited[nx] = 1
                    q.append((nx, cnt + 1))


if N == K:
    print(0)
else: 
    bfs(N)