from collections import deque

def solution(queue1, queue2):
    answer = 0
    d1, d2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(d1), sum(d2)
    
    if (sum1 + sum2) % 2 != 0:
        return -1
    
    target = (sum1+sum2) //2 
    max_ops = len(d1) * 3
    
    while answer <= max_ops:
        if sum1 == target:
            return answer
        if sum1 > target:
            v = d1.popleft()
            d2.append(v)
            sum1 -= v
        else:
            v = d2.popleft()
            d1.append(v)
            sum1 += v
        answer += 1 
    return -1