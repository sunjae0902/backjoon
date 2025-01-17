import heapq as hq
def solution(jobs):
    answer = 0
    q = []
    start = -1 # 마지막으로 작업이 완료된 시간
    now, i = 0, 0 # 시간 카운트, 처리 개수
    while i < len(jobs): # 작업 하나를 처리할 때마다
        for job in jobs:
            if start < job[0] <= now: # 요청이 들어오면 힙에 추가
                hq.heappush(q, (job[1], job[0])) # 소요 시간, 요청 시각
        if q:
            dur, req = hq.heappop(q)
            start = now
            now += dur
            answer += now - req
            i += 1
        else:
            now += 1
    return answer // len(jobs)