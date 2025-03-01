def solution(info, n, m):
    INF = 100000
    size = len(info)
    # dp[i][j]: i번째 물건까지 고려 & B의 흔적 갯수가 j일때 A의 최소 흔적 개수 
    dp = [[INF] * m for _ in range(size + 1)]
    dp[0][0] = 0
    for i in range(1, size + 1): # 각 단계마다 2가지의 경우의 수
        a, b = info[i - 1]
        for j in range(m):
            # a를 선택하는 경우 A의 최소 흔적 개수 갱신
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + a)
            # b를 선택하는 경우 A의 최소 흔적 개수 갱신
            if j + b < m: # m보다 작은 경우만 갱신
                # 이번에 b를 선택하는 경우 / 선택하지 않는 경우(=이전단계) 비교
                dp[i][j + b] = min(dp[i][j + b], dp[i - 1][j])
    answer = min(dp[size])
    return -1 if answer >= n else answer