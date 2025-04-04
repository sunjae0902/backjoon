import heapq

def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [-w for w in works]
    heapq.heapify(works)
    # 작업량이 많은 것부터 처리

    for _ in range(n): # 총 n시간 선택
        max_w = heapq.heappop(works)
        heapq.heappush(works, max_w+1) # 1시간씩 줄임
   
    return sum(w**2 for w in works)
