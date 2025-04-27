from collections import deque

def bfs(s, maps, visited):
    res = 0
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    visited[s[0]][s[1]] = 1
    q = deque([s])
    while q:
        now = q.popleft()
        x, y = now
        res += int(maps[x][y]) 
        for dx, dy in move:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and not visited[nx][ny] and maps[nx][ny] != 'X':
                visited[nx][ny] = 1
                q.append((nx, ny))
    return res


def solution(maps):
    answer = []
    visited = [[0 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    maps = list(list(line) for line in maps)

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if not visited[i][j] and maps[i][j] != 'X':
                answer.append(bfs((i, j), maps, visited))
                
    return [-1] if answer == [] else sorted(answer) 