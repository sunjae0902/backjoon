import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
distances = [INF] * (N+1)

for i in range(M):
    a,b,c = map(int, input().split())
    arr[a].append((b,c))
  
S, E = map(int, input().split())

def dijkstra(s):
    q = []
    distances[s] = 0
    heapq.heappush(q, (s,0))
    while q:
        now, cost = heapq.heappop(q)
        if cost > distances[now]: # 현재 노드까지의 최단 거리보다 큰 가중치라면 패스.
            continue
        for i, c in arr[now]:
            cost = distances[now] + c 
            if cost < distances[i]: 
                distances[i] = cost
                heapq.heappush(q, (i, cost))
dijkstra(S)
print(distances[E])