import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
answer = N * M
hq = []
heapq.heappush(hq, (1, (0,0)))

visited = [[0 for _ in range(M)] for _ in range(N)]
dist = [(-1,0), (1,0), (0,1), (0, -1)]
    
while hq:
    cnt, now = heapq.heappop(hq)
    if now == (N-1, M-1):
        answer = min(answer, cnt)
        continue
    for dx, dy in dist:
        nx, ny = now[0]+dx, now[1]+dy
        if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny]:
            visited[nx][ny] = 1
            heapq.heappush(hq, (cnt+1, (nx, ny)))
print(answer)