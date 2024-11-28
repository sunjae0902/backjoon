import sys
from collections import deque
input = sys.stdin.readline



n,m = map(int,input().split())
board = [[] for _ in range(n)]

for row in range(n):
    s1 = list(input().strip())
    for col in range(m):
        if s1[col] == '2':
            sy,sx = row,col
        board[row].append(int(s1[col]))


def bfs(sy,sx):
    queue = deque()
    queue.append((sy,sx,0))
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[sy][sx] = 1
    dy = [0,1,0,-1]
    dx = [1,0,-1,0]
    while queue:
        y,x,cnt = queue.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if -1 < ny < n and -1 < nx < m and not visited[ny][nx]:
                if board[ny][nx] > 2:
                    print("TAK")
                    print(cnt+1)
                    exit()
                elif board[ny][nx] == 0:
                    queue.append((ny,nx,cnt+1))
                    visited[ny][nx] = 1
    print("NIE")
bfs(sy,sx)