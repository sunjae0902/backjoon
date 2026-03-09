from collections import deque

def solution(n, path, order):
    answer = True
    tree = [[] for _ in range(n)]
    for s,e in path:
        tree[s].append(e)
        tree[e].append(s)
    before = {}

    for a, b in order:
        before[b] = a # b이전에 a가 와야 함
        
    if 0 in before: # 엣지 케이스
        return False

    q = deque([(0)])
    visited = [0 for _ in range(n)]
    visited[0] = 1
    wating = {} # 조건 때문에 방문하지 못하고 기다리고 있는 노드
    while q:
        cur = q.popleft()
        if cur in wating:
            wn = wating.pop(cur)
            visited[wn] = 1
            q.append(wn)
        for nxt in tree[cur]:
            if visited[nxt]:
                continue
            if nxt in before and not visited[before[nxt]]:
                wating[before[nxt]] = nxt # nxt를 방문하기 위해 before[nxt] 방문 먼저
                continue
            visited[nxt] = 1
            q.append(nxt)  
    return all(visited) 