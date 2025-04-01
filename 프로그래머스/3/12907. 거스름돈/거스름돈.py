def solution(n, money):
    dp = [0] * (n + 1)
    dp[0] = 1  # 금액 0을 만드는 경우의 수는 1가지 (아무 동전도 사용하지 않는 경우)

    for coin in money:
        for j in range(coin, n + 1):
            dp[j] = (dp[j] + dp[j - coin]) % 1000000007

    return dp[n]
