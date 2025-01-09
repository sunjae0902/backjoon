import sys, heapq
input = sys.stdin.readline
N, M = map(int, input().split())
move = [0] * 101
visited = [0] * 101

for _ in range(N): # 겹치지 않는다
    s, e = map(int, input().split())
    move[s] = e
for _ in range(M):
    s, e = map(int, input().split())
    move[s] = e

q = []
visited[1] = 1
heapq.heappush(q, (0, 1)) # 카운트, 시작점
while q:
    cnt, now = heapq.heappop(q)
    if now == 100:
        print(cnt)
        break
    for d in range(1, 7):
        if 1 <= now+d < 101 and not visited[now+d]:
            visited[now+d] = 1
            if move[now+d] != 0:
                heapq.heappush(q, (cnt+1, move[now+d]))
            else:
                heapq.heappush(q, (cnt+1, now+d))