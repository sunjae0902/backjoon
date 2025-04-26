from collections import deque

def solution(x, y, n):
    answer = int(1e9)
    visited = {x}
    q = deque([(x, 0)])
    while q:
        num, cnt = q.popleft()
        if num == y:
            answer = min(answer, cnt)
        for new in [num+n, num*2, num*3]:
            if 1 <= new <= 1000000 and new not in visited:
                q.append((new, cnt+1))
                visited.add(new)
    return answer if answer < int(1e9) else -1