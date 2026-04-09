import sys
import heapq as hq

input = sys.stdin.readline
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

def dijk(s):
    # 시작 정점에서 모든 정점까지의 최소 거리
    dist = [int(1e9) for _ in range(n+1)]
    dist[s] = 0
    q = []
    hq.heappush(q, (0, s))
    while q:
        cur_dist, now = hq.heappop(q)
        if cur_dist > dist[now]:
            continue
        for next, cost in graph[now]:
            new_dist = cost + cur_dist
            if new_dist < dist[next]:
                dist[next] = new_dist
                hq.heappush(q, (new_dist, next))
    return dist

cost = [0 for _ in range(n+1)]
# 각자 정점에서 x집으로 가는 최소 비용
for s in range(1, n+1):
    dist = dijk(s)
    cost[s] += dist[x]

# x집에서 각자 집으로 가는 최소 비용
for s in range(1, n+1):
    dist = dijk(x)
    cost[s] += dist[s]

print(max(cost))
    
    

