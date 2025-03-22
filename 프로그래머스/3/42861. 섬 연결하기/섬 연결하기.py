import heapq

def solution(n, costs):
    answer = 0
    arr = [[] for _ in range(n)]
    for s, e, w in costs:
        arr[s].append([e,w])
        arr[e].append([s,w])
    
    visited = set()
    q = [[0, 0]] # 가중치, 시작 노드
    count = 0
    while q:
        weight, now = heapq.heappop(q)
        if now in visited:
            continue
        visited.add(now) # 가장 최소인 노드 방문 표시.
        answer += weight
        count += 1
        if count == n:
            break
        for v, w in arr[now]:
            if v not in visited:
                heapq.heappush(q, [w, v])
    
    return answer