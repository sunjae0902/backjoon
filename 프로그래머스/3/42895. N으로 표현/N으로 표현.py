def calculate(a, b):
    result = {a+b, a-b, a*b}
    if b != 0:
        result.add(a//b)
    return result

def solution(N, number):
    dp = [set() for i in range(9)]
    # 매 단계마다 앞뒤에 N을 추가하는데, 이전 단계 값을 사용해서. 
    dp[1] = {N}
    
    for i in range(2, 9):
        dp[i].add(int(str(N)*i))
        for j in range(1, i):
            for a in dp[j]: # 모든 경우의 수
                for b in dp[i-j]:
                    dp[i].update(calculate(a,b))
    
    for i in range(1, 9):
        if number in dp[i]:
            return i
    return -1