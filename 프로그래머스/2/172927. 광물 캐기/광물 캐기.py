import heapq

def solution(picks, minerals):
    answer = int(1e9)
    arr = [[1,1,1],[5,1,1],[25,5,1]]
    hq = []
    n = len(minerals)
    heapq.heappush(hq, (0, n, picks[:]))
    while hq:
        cost, cnt, cpicks = heapq.heappop(hq)
        if cnt == 0 or set(cpicks) == {0}:
            answer = min(answer, cost)
            continue
        for i in range(len(cpicks)):
            if cpicks[i] > 0:
                npicks = cpicks[:]
                npicks[i] -= 1
                new_cost = cost 
                ncnt = cnt % 5 if cnt // 5 < 1 else 5 # 곡괭이 사용 가능 횟수
                for j in range(ncnt):
                    mineral = minerals[n-cnt + j]
                    if mineral == "diamond":
                        new_cost += arr[i][0]
                    elif mineral == "iron":
                        new_cost += arr[i][1]
                    else: 
                        new_cost += arr[i][2]
                heapq.heappush(hq, (new_cost, cnt - ncnt, npicks))
    return answer