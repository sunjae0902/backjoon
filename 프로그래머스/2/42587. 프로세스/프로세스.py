from collections import deque

def solution(priorities, location):
    answer = 0
    n = len(priorities)
    q = deque([])
    
    for i in range(n):
        q.append((priorities[i], i))
        
    order = [0] * n  
    cnt = 1
    while q:
        max_val = max(q)
        while q[0][0] < max_val[0]:
            q.append(q.popleft())
        now = q.popleft()
        order[now[1]] = cnt
        cnt += 1
        
    answer = order[location]
    return answer