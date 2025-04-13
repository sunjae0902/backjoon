def solution(n):
    answer = [[0 for _ in range(1, i+1)] for i in range(1, n+1)]
    num = 1
    r, c = -1, 0
    for i in range(n): 
        for _ in range(i, n):
            if i % 3 == 0:
                r += 1
            elif i % 3 == 1:
                c += 1
            else:
                r -= 1
                c -= 1
            answer[r][c] = num
            num += 1
    return sum(answer, [])