# 06:58 시작

def solution(n, results):
    answer = 0
    # A < B, B < C이면 A<B<C
    info = [[0 for _ in range(n+1)] for _ in range(n+1)] # 1: 이김, -1: 짐, 0: 모름
    for w, l in results:
        info[w][l] = 1
        info[l][w] = -1
    
    for i in range(n+1):
        for j in range(n+1):
            for k in range(n+1):
                if info[j][i] == 1 and info[i][k] == 1:
                    info[j][k] = 1
                    info[k][j] = -1
    for i in range(1, n+1):
        w, l = info[i].count(1), info[i].count(-1)
        if w+l == n-1:
            answer += 1
    
    return answer