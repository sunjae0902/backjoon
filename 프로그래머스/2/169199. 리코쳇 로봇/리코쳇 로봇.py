import heapq

def solution(board):
    answer = -1
    n = len(board)
    m = len(board[0])
    def bfs(s):
        res = int(1e9)
        dist = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[0 for _ in range(m)] for _ in range(n)]
        visited[s[0]][s[1]] = 1
        q = []
        heapq.heappush(q, (0, s))
        while q:
            cnt, now = heapq.heappop(q)
            if board[now[0]][now[1]] == 'G':
                res = min(res, cnt)
                continue
            for d in dist:
                nr, nc = now[0], now[1]
                while True:
                    nr += d[0]
                    nc += d[1]
                    if nr < 0 or nc < 0 or nr >= n or nc >= m:
                        break
                    if board[nr][nc] == 'D':
                        break
                if not visited[nr-d[0]][nc-d[1]]:
                    visited[nr-d[0]][nc-d[1]] = 1
                    heapq.heappush(q, (cnt+1, (nr-d[0], nc-d[1])))
        return -1 if res == int(1e9) else res
                
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                answer = bfs((i, j)) 
                break
    return answer