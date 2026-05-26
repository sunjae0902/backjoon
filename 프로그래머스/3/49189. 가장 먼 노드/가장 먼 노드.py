from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]

    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)

    dist = [-1] * (n+1) # bfs 1번에 1번 출발의 모든 최단거리 계산 가능
    dist[1] = 0

    q = deque([1])

    while q:
        cur = q.popleft()

        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    max_dist = max(dist)
    return dist.count(max_dist)