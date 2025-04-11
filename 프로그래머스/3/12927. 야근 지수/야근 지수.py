import heapq
def solution(n, works):
    works = [-w for w in works]
    heapq.heapify(works)
    for i in range(n):
        if not works:
            break
        now = heapq.heappop(works)
        if -now > 1:
            heapq.heappush(works, now+1)
        
    return sum([(-i)**2 for i in works])