import heapq
def solution(scoville, K):
    answer = 0
    hq = []
    for s in scoville:
        heapq.heappush(hq, s) 
    while hq:
        if len(hq) == 1:
            if hq[0] < K:
                answer = -1
            break
        mix = [heapq.heappop(hq), heapq.heappop(hq)]
        if mix[0] < K:
            heapq.heappush(hq, mix[0]+2*mix[1])
            answer += 1
        
    return answer