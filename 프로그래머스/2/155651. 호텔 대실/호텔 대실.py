import heapq

def to_min(s):
    return int(s[:2]) * 60 + int(s[3:])

def solution(book_time):
    answer = 1
    book_time.sort(key = lambda x: to_min(x[0]))
    
    hq = []
    for s, e in book_time:
        s_min, e_min = to_min(s), to_min(e)
        while hq and hq[0] + 10 <= s_min:
            heapq.heappop(hq)
        heapq.heappush(hq, e_min)
        answer = max(answer, len(hq))
    return answer