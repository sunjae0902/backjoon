import heapq
def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N)]
    for a, b, c in road:
        graph[a-1].append((b-1, c))
        graph[b-1].append((a-1, c))
        
    dist = [int(1e9)] * N
    dist[0] = 0

    q = [(0, 0)] #거리, 정점
    while q:
        cost, now = heapq.heappop(q)
        if cost > dist[now]: # 더 이상 탐색할 필요 업ㅅ음
            continue
        for e, c in graph[now]:
            new_cost = cost + c
            if dist[e] > new_cost:
                dist[e] = new_cost
                heapq.heappush(q, (new_cost, e))
    for d in dist:
        if d <= K:
            answer += 1
    
    
    return answer