import heapq as hq  
def solution(n, edge):
    answer = 0
    arr = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    visited[1] = 1
    for s,e in edge:
        arr[s].append(e)
        arr[e].append(s)
    
    q = [(0,1)]
    dist = [0 for _ in range(n+1)]
    while q:
        shortest, cur = hq.heappop(q)
        dist[cur] = shortest
        for dest in arr[cur]:
            if not visited[dest]:
                visited[dest] = 1
                hq.heappush(q, (shortest + 1, dest))
    max_dist = max(dist)
    for d in dist:
        if d == max_dist:
            answer += 1
    return answer