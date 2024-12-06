import sys
input = sys.stdin.readline
N = int(input())

arr = [[0] for _ in range(N) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
# dp[i][j]: (i,j)에서 오른쪽끝으로 가는 경우의 수

for i in range(N):
    arr[i] = list(map(int, input().split()))

for i in range(N - 1, -1, -1):
    for j in range(N - 1, -1, -1):
        if i == N - 1 and j == N - 1:
            dp[i][j] = 1 # 주의, 0개가 아니라 1개임
            continue
        jump = arr[i][j]
        if jump == 0:
            dp[i][j] = 0  
        else:
            # 오른쪽으로 이동 가능한 경우 -> 합해줌
            if j + jump < N:
                dp[i][j] += dp[i][j + jump]
            # 아래로 이동 가능한 경우 -> 합해줌
            if i + jump < N:
                dp[i][j] += dp[i + jump][j]

print(dp[0][0])