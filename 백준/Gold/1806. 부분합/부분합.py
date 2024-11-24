import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
min = float("INF")
sum = arr[0]
# end - start가 최소
while(start < N and end < N):
    if sum < S:
        end += 1
        if end == N:
            break
        sum += arr[end]
    else: 
        if min > (end - start + 1):
            min = end - start + 1
        sum -= arr[start]
        start += 1
print(0 if min == float("INF") else min)