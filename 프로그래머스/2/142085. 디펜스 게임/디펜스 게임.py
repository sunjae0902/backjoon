import heapq

def solution(n, k, enemy):
    heap = []
    for i in range(len(enemy)):
        heapq.heappush(heap, -enemy[i])  # 최대 힙 구현
        n -= enemy[i]

        if n < 0:
            if k == 0:
                return i
            largest = -heapq.heappop(heap)  # 가장 많이 소모된 병사 수 되돌리기
            n += largest
            k -= 1
            
    return len(enemy)
