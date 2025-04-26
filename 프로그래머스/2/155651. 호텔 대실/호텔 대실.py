import heapq

def to_min(s):
    return 60 * int(s[:2]) + int(s[3:])

def solution(book_time):
    answer = 0
    book_time.sort(key=lambda x: to_min(x[0]))  # 시작 시간 기준으로 정렬
    hq = []

    for s, e in book_time:
        s_min = to_min(s)
        e_min = to_min(e)
        temp = []
        assigned = False
        
        while hq:
            now = heapq.heappop(hq)
            if now + 10 <= s_min:
                heapq.heappush(hq, e_min)
                assigned = True
                break
            else:
                temp.append(now)
        
        for t in temp: # 복구
            heapq.heappush(hq, t)
        
        if not assigned: # 체크
            heapq.heappush(hq, e_min)
            answer += 1

    return answer
