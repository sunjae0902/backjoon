def solution(plans):
    answer = []
    tmp = []
    for p in plans:
        n, s, t = p[0], p[1], [2]
        h, m = map(int, s.split(':'))
        p[1] = 60 * h + m
        p[2] = int(p[2])
        
    plans.sort(reverse = True, key = lambda x: x[1])
    
    while plans:
        if len(plans) == 1:
            answer.append(plans.pop()[0])
            break
        i = len(plans)-1
        end = sum(plans[i][1:3])
        next_start = plans[i-1][1]
        if end == next_start:
            answer.append(plans.pop()[0])
        # 진행 중이던 과제를 마치고 새 과제 까지 시간이 남을 경우 -> 멈췄던 과제 진행
        elif end < next_start:
            answer.append(plans.pop()[0])
            dur = next_start - end
            while tmp and dur > 0:
                now = tmp.pop()
                if dur >= now[2]:
                    answer.append(now[0])
                    dur -= now[2]
                else:
                    now[2] -= dur
                    tmp.append(now)
                    dur = 0
        else:
            plans[i][1] = next_start
            plans[i][2] = end - next_start
            tmp.append(plans[i])
            plans.pop()
    while tmp:
        answer.append(tmp.pop()[0])
    return answer