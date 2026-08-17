def digit(n):
    res = []
    while n > 0:
        n -= 1
        res.append('124'[n%3])
        n //= 3
    return res[::-1]

def solution(n):
    answer = ''.join(digit(n))
    return answer