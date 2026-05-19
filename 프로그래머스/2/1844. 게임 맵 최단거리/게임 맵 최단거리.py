from collections import deque
def solution(maps):
    answer = int(1e9)
    n, m = len(maps), len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    move = [(0, 1), (0, -1), (1, 0), (-1,0)]
    q = deque([(0, 0, 0)])
    while q:
        r, c, cnt = q.popleft()
        if (r, c) == (n-1, m-1):
            answer = min(answer, cnt)
        for dr, dc in move:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and maps[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc, cnt+1))
    
    return answer+1 if answer != int(1e9) else -1