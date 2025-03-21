from collections import deque

def bfs(s, visited, computers):
    q = deque([s])
    visited[s] = 1
    while q:
        now = q.popleft()
        for i, v in enumerate(computers[now]):
            if not visited[i] and v == 1:
                visited[i] = 1
                q.append(i)
    return 1
                
def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            answer += bfs(i, visited, computers)
    return answer