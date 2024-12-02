import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split())) # 0 - n-1
dp = [1] * N # i+1번째 원소를 마지막으로 넣었을때, 가장 긴 감소하는 수열의 길이

for i in range(1, N): # arr[1], 즉 2번째 아이템부터
    last = arr[i]
    for j in range(i):
        if last < arr[j]:  # 감소하는 수열인 경우에만 갱신
            dp[i] = max(dp[i], dp[j]+1) # 기존 값, 새로운 arr[j] 를 넣었을 경우 길이 비교 ->
print(max(dp))