import sys, heapq
input = sys.stdin.readline
N, K = map(int, input().split())
dist = [int(1e9)] * (1000001)
pos = N
q = []
heapq.heappush(q, (0, pos))
while q:
    c, n = heapq.heappop(q)
    if n == K:
        print(c)
        break
    if dist[n] < c:
        continue
    for d in [(1, -1), (1, 1), (0, n)]:
        if 0 <= n+d[1] < 1000001 and dist[n+d[1]] > c+d[0]:
            dist[n+d[1]] = c+d[0]
            heapq.heappush(q, (c+d[0], n+d[1]))