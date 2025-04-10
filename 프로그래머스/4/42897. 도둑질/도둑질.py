def get_max(money):
    n = len(money)
    dp = [0] * n # i집까지 고려했을 때, 최대 금액
    dp[0] = money[0] 
    dp[1] = max(money[0], money[1])
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    return dp[-1]
    
def solution(money):
    # 첫번째 집을 포함하고 마지막 집을 빼거나, 첫번째 집을 빼고 마지막 집을 넣는 경우
    return max(get_max(money[:-1]), get_max(money[1:]))