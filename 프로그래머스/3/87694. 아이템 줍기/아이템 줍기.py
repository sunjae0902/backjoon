from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    path = [[0 for _ in range(101)] for _ in range(101)]
    rectangle = [(x1*2, y1*2, x2*2, y2*2) for x1, y1, x2, y2 in rectangle]
    
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1+1, x2):
            for y in range(y1+1, y2):
                path[x][y] = 1
       
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                if x in [x1, x2] or y in [y1, y2]:
                    if path[x][y] != 1:
                        path[x][y] = 2
                           
    def bfs():
        visited = [[0 for _ in range(101)] for _ in range(101)]
        s, e = (characterX*2, characterY*2), (itemX*2, itemY*2)
        q = deque([(s, 0)])
        visited[s[0]][s[1]] = 1
        move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        while q:
            now, cnt = q.popleft()
            if now == e:
                return cnt//2
            for dx, dy in move:
                nx, ny = now[0]+dx, now[1]+dy
                if 0 < nx < 101 and 0 < ny < 101 and not visited[nx][ny] and path[nx][ny] == 2:
                    q.append(((nx, ny), cnt+1))
                    visited[nx][ny] = 1
        
    return bfs()