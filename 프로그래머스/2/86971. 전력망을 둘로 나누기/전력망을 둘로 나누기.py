
def solution(n, wires):
    answer = n
    tree = [[] for _ in range(n+1)]
    
    for w in wires:
        tree[w[0]].append(w[1])
        tree[w[1]].append(w[0])

    def dfs(s, e):
        cnt = 1
        visited = [0] * (n+1)
        stack = [s]
        visited[s] = 1
        while stack:
            now = stack.pop()
            for v in tree[now]:
                if not visited[v] and v != e:
                    visited[v] = 1
                    cnt += 1
                    stack.append(v)
        return cnt
    
    for w in wires:
        cnt = dfs(w[0], w[1])
        answer = min(answer, abs(n-2*cnt))
        
    return answer