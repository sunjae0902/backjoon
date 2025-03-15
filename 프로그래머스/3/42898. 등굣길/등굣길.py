def solution(m, n, puddles):
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[1][1] = 1
    
    for i in range(1, n+1): #거꾸로 주의
        for j in range(1, m+1):
            if [j, i] in puddles:
                dp[i][j] = -1
                
    for i in range(2, m+1):
        if dp[1][i] != -1:
            dp[1][i] = dp[1][i-1]       
    for i in range(2, n+1):
        if dp[i][1] != -1:
            dp[i][1] = dp[i-1][1]
            
    for i in range(2, n+1):
        for j in range(2, m+1): 
            cnt = 0
            if dp[i][j] == -1:
                continue
            if dp[i-1][j] != -1:
                cnt += dp[i-1][j]
            if dp[i][j-1] != -1:
                cnt += dp[i][j-1]
            dp[i][j] = cnt % 1000000007
    return dp[n][m]