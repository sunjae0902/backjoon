from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2) # 양방향 덱
    sum1, sum2 = sum(q1), sum(q2)
    total = sum1 + sum2

    if total % 2 != 0:  # 합이 홀수면 x
        return -1

    target = total // 2
    max_ops = len(queue1) * 3 # 모든 수를 교환해도 안 되는 경우가 상한선
    ops = 0
    p1, p2 = 0, 0 

    while ops <= max_ops: # 균형이 맞을 때까지 연산 반복
        if sum1 == target:
            return ops
        elif sum1 > target: # 더 큰 쪽에서 제거 
            val = q1.popleft()
            sum1 -= val
            q2.append(val)
        else:
            val = q2.popleft()
            sum2 -= val
            q1.append(val)
            sum1 += val
        ops += 1

    return -1
