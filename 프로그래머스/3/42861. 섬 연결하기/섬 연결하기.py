import heapq

def solution(n, costs):
    arr = [[] for _ in range(n)]
    for s, e, w in costs:
        arr[s].append((w, e))
        arr[e].append((w, s))

    def prim():
        hq = [(0, 0)]  # (가중치, 시작 노드)
        visited = [0] * n
        total_weight = 0
        count = 0  # 간선 개수
        
        while hq:
            w, node = heapq.heappop(hq)
            if visited[node]:
                continue
            visited[node] = True
            total_weight += w
            count += 1
            if count == n:  # 모든 노드가 연결되면 종료
                break
            for nw, next_node in arr[node]:
                if not visited[next_node]:
                    heapq.heappush(hq, (nw, next_node))     
        return total_weight

    return prim()
