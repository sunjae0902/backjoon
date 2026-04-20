import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
move = [(0,1), (0,-1), (1, 0), (-1,0)]
map = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
q = deque([(0, 0, 1, False)])
visited[0][0][0] = 1 # 벽을 부수지 않은 상태로 방문
answer = int(1e9)

while q:
    x, y, dist, flag = q.popleft()
    if (x,y) == (n-1, m-1):
        answer = min(answer, dist)
        continue
    for dx, dy in move:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m:
            if flag: # 이미 부심 -> 0인 곳만 이동 가능
                if map[nx][ny] == 0 and not visited[nx][ny][1]:
                    q.append((nx, ny, dist+1, True))
                    visited[nx][ny][1] = 1 
            else:
                if map[nx][ny] == 0 and not visited[nx][ny][0]:
                    q.append((nx, ny, dist+1, False))
                    visited[nx][ny][0] = 1
                elif map[nx][ny] == 1 and not visited[nx][ny][1]:
                    q.append((nx, ny, dist+1, True))
                    visited[nx][ny][1] = 1
                    
print(answer if answer != int(1e9) else -1)
