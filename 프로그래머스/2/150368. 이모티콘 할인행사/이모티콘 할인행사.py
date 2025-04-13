from itertools import product

def solution(users, emoticons):
    answer = [0, 0]
    n = len(emoticons)
    for pd in product([10, 20, 30, 40], repeat = n):
        cnt, cost = 0, 0
        for ratio, limit in users:
            sum_cost = 0
            for i in range(n):
                if pd[i] >= ratio:
                    sum_cost += emoticons[i] - emoticons[i] * pd[i] // 100
            if sum_cost >= limit:
                cnt += 1
            else:
                cost += sum_cost
        if cnt > answer[0] or (cnt == answer[0] and cost > answer[1]):
            answer = [cnt, cost]  
    return answer