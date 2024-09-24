import sys
input = sys.stdin.readline
N = int(input())
ans = 0
arr = list(map(int, input().split()))
arr.sort()
for i in range(N-1):
    arr[i+1] += arr[i]
    ans += arr[i]
ans += arr[N-1]
print(ans)
