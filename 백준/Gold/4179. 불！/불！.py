import sys
from collections import deque

input = sys.stdin.readline
r, c = map(int, input().split())
miro = []
visited = [[0 for _ in range(c)] for _ in range(r)]
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
q = deque()
fire = deque()

for i in range(r):
    col = list(input().strip())
    miro.append(col)
    for j in range(c):
        if col[j] == 'J':
            visited[i][j] = 1
            q.append((i, j))
            miro[i][j] = '.'
        elif col[j] == 'F':
            fire.append((i, j))

minute = 0
while q:
    minute += 1
    
    for _ in range(len(q)): 
        x, y = q.popleft()
        if (x in [0, r-1] or y in [0, c-1]) and miro[x][y] == '.':   
            print(minute)
            exit()
        for dx, dy in move:
            nx, ny = x+dx, y+dy
            if 0 <= nx < r and 0 <= ny < c and miro[nx][ny] == '.' and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = 1
    for _ in range(len(fire)): # 불 확산
        fx, fy = fire.popleft()
        for dx, dy in move:
            nx, ny = fx + dx, fy + dy
            if 0 <= nx < r and 0 <= ny < c and miro[nx][ny] == '.':
                miro[nx][ny] = 'F'
                fire.append((nx, ny))

print("IMPOSSIBLE")
