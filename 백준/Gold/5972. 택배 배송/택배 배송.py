import sys, heapq
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
dist = [int(1e9) for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))
h = []
heapq.heappush(h, (0, 1))
dist[1] = 0 # i번째 노드까지 왔을때 최소 비용
while h:
    cnt, now = heapq.heappop(h)
    for v, c in arr[now]: 
        if dist[v] > cnt + c:
            dist[v] = cnt + c
            heapq.heappush(h, (cnt + c, v))
print(dist[N])