from collections import deque

def bfs(n, graph):
    max_depth, count = 0, 0
    q = deque([(1, 0)])
    visited = [0] * (n+1)
    visited[1] = 1
    while q:
        now, depth = q.popleft()
        if depth > max_depth:
            max_depth = depth
            count = 0
        if depth == max_depth:
            count += 1
        for v in graph[now]:
            if not visited[v]:
                q.append((v, depth+1))
                visited[v] = 1
    return count
          
def solution(n, edge):
    arr = [[] for _ in range(n+1)]
    
    for s,e in edge:
        arr[s].append(e)
        arr[e].append(s)

    return bfs(n, arr)