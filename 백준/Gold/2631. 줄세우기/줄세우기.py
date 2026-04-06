import sys
input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
# 아이디어: 안움직여도 되는 아이들(증가하는 부분수열)을 최대로(가장 긴) 하자
# 가장 긴 증가하는 부분수열: 수열의 매 자리에서 끝날 때 증가하는 부분수열을 모두 구해서 최댓값 찾기
dp = [1] * n  # dp[i] = i에서 끝나는 LIS 길이

for i in range(n):
    for j in range(i): # 이중 반복으로 비교
        if arr[j] < arr[i]: # 오름차순일 경우 수열 길이 +1
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
