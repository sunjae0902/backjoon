def solution(n, computers):
    answer = 0
    parents = [i for i in range(n)]
    connected = [[] for _ in range(n)]
    
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(a, b):
        pa, pb = find(a), find(b)
        if pa != pb:
            parents[pa] = pb
    
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                union(i, j)
    answer = len(set(find(i) for i in range(n)))
    return answer