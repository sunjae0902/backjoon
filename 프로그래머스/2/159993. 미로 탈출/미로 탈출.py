from collections import deque

def bfs(s, e, maps):
    res, n, m = int(1e9), len(maps), len(maps[0])
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[s[0]][s[1]] = 1
    q = deque([(s, 0)])
    while q:
        now, dist = q.popleft()
        if now == e:
            res = min(res, dist)
        for dx, dy in move:
            nx, ny = now[0]+dx, now[1]+dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                q.append(([nx, ny], dist+1))
                visited[nx][ny] = 1
    return res

def solution(maps):
    s, e, lv = [], [], []
    maps = list(list(line) for line in maps)
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                s = [i, j]
            if maps[i][j] == 'L':
                lv = [i, j]
            if maps[i][j] == 'E':
                e = [i, j]
    f, s = bfs(s, lv, maps), bfs(lv, e, maps)
    
    if f < int(1e9) and s < int(1e9):
        return f+s
    return -1