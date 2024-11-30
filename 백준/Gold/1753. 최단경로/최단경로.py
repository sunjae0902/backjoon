import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
S = int(input())
arr = [[] for _ in range(V + 1)]
distances = [INF] * (V+1)

for i in range(E):
    a, b, c = map(int, input().split())
    arr[a].append((b,c))
    

def dijkstra(s):
    q = []
    heapq.heappush(q, (0, s))
    distances[s] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distances[now] < dist:
            continue
        for i, c in arr[now]:
            cost = distances[now] + c
            if cost < distances[i]:
                distances[i] = cost
                heapq.heappush(q, (cost, i))
dijkstra(S)
for i in range(1, V+1):
    print(distances[i] if distances[i] != INF else "INF")