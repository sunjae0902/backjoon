from collections import deque

def solution(n, edge):
    answer = []
    graph = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    visited[1] = 1
    q = deque([(0, 1)]) # 최단거리, N번노드까지
    for s,e in edge:
        graph[s].append(e)
        graph[e].append(s)
    while q:
        dist, node = q.popleft()
        answer.append(dist)
        for n in graph[node]:
            if visited[n]:
                continue
            visited[n] = 1
            q.append((dist+1, n))

    return len([i for i in answer if i == max(answer)])