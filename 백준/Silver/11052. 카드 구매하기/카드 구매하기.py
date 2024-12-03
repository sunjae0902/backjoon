import sys
input = sys.stdin.readline
N = int(input())
price = list(map(int, input().split()))

dp = [[0 for _ in range(N+1)] for _ in range(N+1)] 
# i번째 아이템을 마지막으로 j개 샀을 경우 최대비용

for i in range(1, N+1):
    for j in range(1, N+1):
        if i > j: # 살 수 없는 경우, 이전 단계 값으로 갱신
            dp[i][j] = dp[i-1][j]
        else:
            # i번째 아이템을 사용하지 않는 경우, 사용하는 경우(현재 물건의 가격 + '현재 물건 포함했을때' 합이 j-i가 되는 가격)
            dp[i][j] = max(dp[i-1][j], price[i-1]+ dp[i][j - i])

print(dp[N][N])