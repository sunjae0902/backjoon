import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dist = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 북, 동, 남, 서에서 한 칸 전진
q = deque([(r,c,d)])
answer = 0
while q:
    nowr, nowc, nowd = q.popleft()
    if arr[nowr][nowc] == 0:
        answer += 1
        arr[nowr][nowc] = 2
    isExist = 0 in [arr[nowr+dx][nowc+dy] for dx, dy in dist]
    if not isExist:
        nr, nc = nowr + dist[nowd][0] * -1, nowc + dist[nowd][1] * -1
        # 벽이 아닐 경우
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 1:
            q.append((nr, nc, nowd))
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:
            break
    else:
        nd = 3 if nowd == 0 else nowd - 1 # 회전
        nr, nc = nowr + dist[nd][0], nowc + dist[nd][1]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
            arr[nr][nc] = 2 # 1이 아닌 값으로
            answer += 1
            q.append((nr, nc, nd))
        else:
            q.append((nowr, nowc, nd)) # 전진할 수 없을 경우, 방향만 바꿈
print(answer)