def solution(info, edges):
    answer = 0
    tree = [[] for _ in range(len(info))]
    
    for p, c in edges:
        tree[p].append(c)
        tree[c].append(p)
    
    def dfs(node, s, w, path):
        nonlocal answer
        answer = max(answer, s)
        for pv in path:
            for v in tree[pv]:
                if v not in path:
                    ns, nw = s + (1 if info[v] == 0 else 0), w + (1 if info[v] == 1 else 0)
                    if ns > nw:
                        dfs(v, ns, nw, path + [v])
       

    dfs(0, 1, 0, [0])
    return answer