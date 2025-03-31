from collections import deque

def bfs(info, graph):
    max_sheep = 0
    queue = deque([(0, 1, 0, [0])])  # (현재 노드, 양 수, 늑대 수, 방문 경로)

    while queue:
        node, sheep, wolf, visited = queue.popleft()
        max_sheep = max(max_sheep, sheep)
        
        # 현재 노드에서 갈 수 있는 경로 탐색
        for next_node in graph[node]:
            if next_node not in visited:
                new_visited = visited + [next_node]
                next_sheep = sheep + (1 if info[next_node] == 0 else 0)
                next_wolf = wolf + (1 if info[next_node] == 1 else 0)

                if next_sheep > next_wolf:
                    queue.append((next_node, next_sheep, next_wolf, new_visited))

        # 이전 경로로 다시 돌아가서 또 다른 노드 탐색
        for v in visited:
            for next_node in graph[v]:
                if next_node not in visited:
                    new_visited = visited + [next_node]
                    next_sheep = sheep + (1 if info[next_node] == 0 else 0)
                    next_wolf = wolf + (1 if info[next_node] == 1 else 0)

                    if next_sheep > next_wolf:
                        queue.append((next_node, next_sheep, next_wolf, new_visited))

    return max_sheep

def solution(info, edges):
    n = len(info)
    graph = [[] for _ in range(n)]

    for parent, child in edges:
        graph[parent].append(child)
        graph[child].append(parent)

    answer = bfs(info, graph)
    return answer
