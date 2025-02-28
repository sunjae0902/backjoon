import sys
from collections import deque
input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())
answer = int(1e9)
visited = [0] * (F+1)
q = deque([(S, 0)])
visited[S] = 1
while q:
    now, cnt = q.popleft()
    if now == G:
        answer = min(answer, cnt)
        continue
    for d in [U, -D]:
        new_floor = now + d
        if 1 <= new_floor <= F and not visited[new_floor]:
            visited[new_floor] = 1
            q.append((new_floor, cnt+1))
if answer == int(1e9):
    print("use the stairs")
else:
    print(answer)