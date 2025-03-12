
    
def solution(n, wires):
    answer = n
    tree = [[] for _ in range(n+1)]
    for w in wires:
        tree[w[0]].append(w[1])
        tree[w[1]].append(w[0])

    def dfs(s, parent):
        visited[s] = 1
        count = 1
        for v in tree[s]:
            if not visited[v] and v != parent:
                visited[v] = 1
                count += dfs(v, s)
        return count
    
    for w in wires:
        visited = [0] * (n+1)
        answer = min(answer, abs(n-2*dfs(w[1], w[0])))
    return answer