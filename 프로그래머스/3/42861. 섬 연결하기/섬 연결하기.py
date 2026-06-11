def solution(n, costs):
    parent = list(range(n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b):
        a = find(a)
        b = find(b)

        if a != b:
            parent[a] = b
            return True # 합 집합인거고
        return False # 못합한거

    costs.sort(key=lambda x: x[2]) # 비용 적은 순 정렬

    answer = 0

    for a, b, cost in costs:
        if union(a, b): # 합해지면
            answer += cost

    return answer