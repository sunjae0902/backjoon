def solution(land, height):
    n = len(land)
    edges = []

    def idx(r, c): # 정점 번호 지정
        return r * n + c

    move = [(1,0),(0,1)]  # 중복 방지 (무방향 그래프이므로)

    for r in range(n):
        for c in range(n):
            for dr, dc in move:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n:
                    diff = abs(land[r][c] - land[nr][nc])
                    cost = 0 if diff <= height else diff
                    edges.append((cost, idx(r,c), idx(nr,nc))) ## 모든 간선 비용 저장 (비용,출발,도착)

    parent = list(range(n*n)) # 각 노드가 속한 집합의 루트 노드 저장 0~n**2-1
    def find(x):# 부모의 부모~로 타고 올라가서 루트 부모 찾음
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)
        if a == b: # 같으면 연결 못함
            return False
        parent[b] = a
        return True

    edges.sort() # 간선 비용을 오름차순으로 정렬!
    answer = 0

    for cost, u, v in edges:
        if union(u, v):
            answer += cost

    return answer