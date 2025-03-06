def solution(triangle):
    answer = 0
    n = len(triangle)
    dp = [[0 for _ in range(i+1)] for i in range(n)] # 마지막 기준 최댓값 저장
    dp[0][0] = triangle[0][0] 
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][0]
                continue
            elif j == i:
                dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                continue
            dp[i][j] = triangle[i][j] + max(dp[i-1][j], dp[i-1][j-1])
    answer = max(dp[n-1])

    return answer