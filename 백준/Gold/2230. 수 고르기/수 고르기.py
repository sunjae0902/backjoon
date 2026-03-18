import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
arr.sort()
s,e = 0,0
answer = int(2e9)
# 현재만 보고 판단해야 함
while s < n and e < n: 
    if arr[e] - arr[s] < m:
        e += 1
    else:
        answer = min(answer, arr[e] - arr[s])
        s += 1
print(answer)