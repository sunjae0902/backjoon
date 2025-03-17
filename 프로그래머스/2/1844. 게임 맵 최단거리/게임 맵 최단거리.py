from collections import deque

def bfs(maps):
    move = [(0, -1), (0, 1), (1, 0), (-1, 0)]
    n, m = len(maps), len(maps[0])
    res = n * m + 1
    s = (0,0)
    q = deque([(1, s)])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    while q:
        cnt, now = q.popleft()
        if now == (n-1, m-1):
            res = min(res, cnt)
        for x, y in move:
            nx, ny = now[0]+x, now[1]+y
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                q.append((cnt+1, (nx, ny)))
                visited[nx][ny] = 1
    return res if res != n*m + 1 else -1
        
def solution(maps):
    answer = bfs(maps)
    return answer