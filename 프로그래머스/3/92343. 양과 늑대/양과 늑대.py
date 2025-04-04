from collections import deque

def bfs(info, tree):
    max_sheep = 1
    q = deque([(0, 1, 0, [0])]) # 현재노드, 양의 수, 늑대수, 현재 경로
    
    while q:
        now, s, w, path = q.popleft()
        max_sheep = max(max_sheep, s)
        
        for v in tree[now]:
            if v not in path:
                ns, nw = s + (1 if info[v] == 0 else 0), w + (1 if info[v] == 1 else 0)
                if ns > nw:
                    q.append((v, ns, nw, path + [v]))
        
        for pv in path:
            for v in tree[pv]:
                if v not in path:
                    ns, nw = s + (1 if info[v] == 0 else 0), w + (1 if info[v] == 1 else 0)
                    if ns > nw:
                        q.append((v, ns, nw, path + [v]))
        
    return max_sheep
        

def solution(info, edges):
    tree = [[] for _ in range(len(info))]
    for p, c in edges:
        tree[p].append(c)
        tree[c].append(p)
    
    return bfs(info, tree)