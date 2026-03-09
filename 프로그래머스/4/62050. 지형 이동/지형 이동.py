from collections import deque

def solution(land, height):
    answer = 0
    move = [(1, 0), (0, 1)]
    # (이동비용, r, c)
    n = len(land)
    edges = [] # i번 노드 ~ j번 노드 간선 최소 비용
    
    for i in range(n):
        for j in range(n):
            for dr, dc in move:
                nr, nc = i+dr, j+dc
                if 0 <= nr < n and 0 <= nc < n:
                    diff = abs(land[i][j] - land[nr][nc])
                    edges.append((diff if diff > height else 0, i*n+j, nr*n+nc))

    edges = sorted(edges)
    parent = [_ for _ in range(n**2)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x]) 
        return parent[x]
        
    def union(a, b):
        pa = find(a)
        pb = find(b)
        if pa == pb:
            return False
        parent[pa] = pb
        return True
    
    for cost, s, e in edges:
        if union(s, e):
            answer += cost
    return answer