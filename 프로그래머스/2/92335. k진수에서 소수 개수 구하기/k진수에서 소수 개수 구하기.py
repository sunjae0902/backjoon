import math

def prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True

def to_k_base(n, k):
    arr = []
    while n >= k:
        arr.append(str(n%k))
        n //= k
    arr.append(str(n))
    return arr[::-1]

def solution(n, k):
    answer = 0
    based = to_k_base(n, k)

    parts = ''.join(based).split('0') # 0을 기준으로 분리!, 0이 없다면, 그대로 들어감

    for part in parts:
        if part == '':  # 빈 문자열 건너뜀
            continue
        num = int(part)
        if prime(num):
            answer += 1
        
    return answer