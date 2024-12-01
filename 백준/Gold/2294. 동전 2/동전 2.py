import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coins = [int(input()) for i in range(N)]
dp = [10001] * (K+1) # dp[i]: 합이 i가 되는데 필요한 동전의 최소 갯수
dp[0] = 0

for coin in coins: # 각 동전을 하나씩 사용한다.
    for i in range(coin, K+1): # 현재 코인보다 큰 값부터 검사. 합해서 i가 됨
        dp[i] = min(dp[i], dp[i-coin]+1) # 이전까지 갱신된 값과, 그 값에서 현재 코인 1개로 대체했을 경우 갯수를 비교해서 더 작은 값을 업데이트
print(dp[K] if dp[K] != 10001 else -1)