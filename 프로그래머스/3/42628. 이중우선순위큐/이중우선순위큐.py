import heapq # 최소 힙
def solution(operations):
    answer = [0,0]
    max_hq, min_hq = [], []
    
    for oper in operations:
        oper = list(oper.split())
        if oper[0] == 'I':
            heapq.heappush(max_hq, (-1) * int(oper[1]))
            heapq.heappush(min_hq, int(oper[1]))
            
        elif oper[1] == '-1':
            if not min_hq:
                continue
            minimum = heapq.heappop(min_hq)
            if -minimum in max_hq:
                max_hq.remove(-minimum)
                heapq.heapify(max_hq)
    
        else:
            if not max_hq:
                continue
            maximum = -heapq.heappop(max_hq)
            if maximum in min_hq:
                min_hq.remove(maximum)
                heapq.heapify(min_hq)
                  
    
    return [-max_hq[0], min_hq[0]] if max_hq and min_hq else [0,0]