def solution(n, wires):
    answer = n
    tree = [[] for _ in range(n+1)]
    
    for w in wires:
        tree[w[0]].append(w[1])
        tree[w[1]].append(w[0])

    def dfs(s, parent):
       
        count = 1
        for v in tree[s]:
            if v != parent:
               
                count += dfs(v, s)
        return count
    
    for w in wires:
      
        answer = min(answer, abs(n-2*dfs(w[1], w[0])))
    return answer