from collections import deque
def go(i, j, storage): # 외부에서 접근 가능한지
    n, m = len(storage), len(storage[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    visited[i][j] = 1
    q = deque([(i, j)])
    dist = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    while q:
        now = q.popleft()
        if now[0] in [0, n-1] or now[1] in [0, m-1]:
            return True
        for d in dist:
            ni, nj = now[0] + d[0], now[1] + d[1]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:
                if storage[ni][nj] == '0':
                    visited[ni][nj] = 1
                    q.append((ni, nj))
    
    return False

def solution(storage, requests):
    n, m = len(storage), len(storage[0])
    storage = [list(s) for s in storage]
    answer = n*m
    
    for rq in requests:
        if len(rq) == 2:
            target = rq[0]
            for i in range(n):
                for j in range(m):
                    if storage[i][j] == target:
                        storage[i][j] = '0'
                        answer -= 1
        else:
            target = rq[0]
            tmp = []
            for i in range(n):
                for j in range(m):
                    if storage[i][j] == target:
                        if go(i, j, storage):
                            tmp.append((i, j))
                            answer -= 1
            for i, j in tmp:
                storage[i][j] = '0'
    return answer
