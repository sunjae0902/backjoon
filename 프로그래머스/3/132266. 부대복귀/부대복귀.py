from collections import deque

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)
    
    # destination에서 출발하는 BFS!(역방향)
    distance = [-1] * (n + 1)
    distance[destination] = 0
    q = deque([destination])
    
    while q:
        now = q.popleft()
        for neighbor in graph[now]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[now] + 1
                q.append(neighbor)
    
    # 각 source에 대해 거리값을 찾아서 answer에 추가
    return [distance[s] for s in sources]
