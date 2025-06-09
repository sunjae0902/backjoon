import heapq
def solution(n, k, enemy):
    hq = []
    for i in range(len(enemy)):
        heapq.heappush(hq, -enemy[i])
        n -= enemy[i]
        if n < 0:
            if k == 0: # 다 소진
                return i
            n -= heapq.heappop(hq) # 가장 많이 사용된 적군에 무적권 사용
            k -= 1
    return len(enemy)