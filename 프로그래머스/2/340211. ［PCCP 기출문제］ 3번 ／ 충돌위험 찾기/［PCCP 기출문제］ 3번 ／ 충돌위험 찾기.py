from collections import defaultdict, deque

def solution(points, routes):
    answer = 0
    # 각 로봇마다의 최단 경로 구하고(모든 경우 탐색할 필요 없이 조건에 맞게 이동), 시간마다 충돌횟수 체크
    min_routes = []

    for route in routes:
        s = points[route[0]-1] 
        sr, sc = s[0], s[1]
        tmp = [s]
        for j in range(1, len(route)):
            e = points[route[j]-1]
            er, ec = e[0], e[1]
            dr, dc = er-sr, ec-sc
            while dr != 0: # 거리가 0이 될 때까지, r 먼저 이동
                if dr > 0:
                    sr += 1
                    dr -= 1
                else:
                    sr -= 1
                    dr += 1
                tmp.append([sr, sc])

            while dc != 0:
                if dc > 0:
                    sc += 1
                    dc -= 1
                else:
                    sc -= 1
                    dc += 1
                tmp.append([sr, sc])
        min_routes.append(tmp)

    sec = max([len(i) for i in min_routes])
    for s in range(sec):
        position_count = defaultdict(int)
        for route in min_routes:
            if s < len(route):
                position_count[tuple(route[s])] += 1
        answer += sum(1 for count in position_count.values() if count > 1)    
    return answer