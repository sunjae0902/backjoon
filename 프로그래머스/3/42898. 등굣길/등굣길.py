from collections import deque

def solution(m, n, puddles):
    answer = 0
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1 # 최단거리 수
    for p in puddles: # 방문 불가
        dp[p[1]-1][p[0]-1] = -1 
        
    for i in range(1, n): # 가장자리 처리
        if dp[i][0] != -1:
            dp[i][0] = dp[i-1][0]
            
    for i in range(1, m):
        if dp[0][i] != -1:
            dp[0][i] = dp[0][i-1]
   
    for i in range(1, n):
        for j in range(1, m):
            cnt = 0
            if dp[i][j] == -1:
                continue
            if dp[i-1][j] != -1:
                cnt += dp[i-1][j]
            if dp[i][j-1] != -1:
                cnt += dp[i][j-1]
            dp[i][j] = cnt % 1000000007
    answer = dp[-1][-1]
    return answer