import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dist = [(-1,0), (0, 1), (1, 0), (0, -1)] # 북 동 남 서 전진
answer = 0
q = deque([(r, c, d)])
while q:
    nowr, nowc, nowd = q.popleft()
    if arr[nowr][nowc] == 0:
        answer += 1
        arr[nowr][nowc] = 2
    is_exist = 0 in [arr[nowr+dx][nowc+dy] for dx, dy in dist]
    if is_exist:
        nowd = 3 if nowd == 0 else nowd-1
        nr, nc = nowr+dist[nowd][0], nowc+dist[nowd][1]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
            q.append((nr, nc, nowd))
        else:
            q.append((nowr, nowc, nowd))
    else:
        nr, nc = nowr + (-1) * dist[nowd][0], nowc + (-1) * dist[nowd][1]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 1:
            q.append((nr, nc, nowd))    
        else:
            break
print(answer)