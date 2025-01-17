def solution(number):
    answer = 0
    def dfs(n, start, cur):
        nonlocal answer # 명시적으로 상위에서 가져옴
        if n == 0:
            if sum(cur) == 0:
                answer += 1
        for i in range(start, len(number)):
            dfs(n-1, i+1, cur+[number[i]])
            
    dfs(3, 0, [])
    return answer