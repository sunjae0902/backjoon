def solution(n, money):
    dp = [0] * (n + 1) # i원 경우의 수
    dp[0] = 1
    for coin in money:
        for j in range(coin, n + 1):
            dp[j] = (dp[j] + dp[j - coin]) % 1000000007

    return dp[n]
