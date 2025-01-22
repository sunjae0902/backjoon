from collections import deque

def solution(land):
    answer = 0
    m = len(land[0])
    n = len(land)
    results = [0] * m
    visited = [[0 for _ in range(m)] for _ in range(n)]
    def bfs(r, c):
        dist = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        s = deque([(r,c)])
        res = 1
        visited_col = {c} # 중복 방지하기 위해 이미 방문한 열에 표시
        while s:
            now = s.popleft()
            for d in dist:
                nr, nc = now[0]+d[0], now[1]+d[1]
                if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                    if land[nr][nc] == 1:
                        res += 1
                        visited[nr][nc] = 1
                        s.append((nr, nc))
                        visited_col.add(nc)
        for c in visited_col:
            results[c] += res
            
    for i in range(m):
        tmp = 0
        for j in range(n):
            if land[j][i] == 1 and not visited[j][i]:
                visited[j][i] = 1
                bfs(j, i)
    answer = max(results) # 시작 행, 열
    return answer