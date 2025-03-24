from collections import defaultdict, deque

def solution(tickets):
    dic = defaultdict(list)
    
    for s, e in sorted(tickets):
        dic[s].append(e)
    
    q = deque([("ICN", ["ICN"], set())])
    
    while q:
        now, path, used = q.popleft()
        
        if len(used) == len(tickets):
            return path
        
        for i, next_dest in enumerate(dic[now]):
            if (now, i) not in used: 
                q.append((next_dest, path + [next_dest], used | {(now, i)}))
    
    return []
