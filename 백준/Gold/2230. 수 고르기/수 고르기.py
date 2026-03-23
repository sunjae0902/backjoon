import sys
input = sys.stdin.readline
n,m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr.sort()
s,e = 0, 1
answer = int(2e9)

while s < n and e < n:
    diff = arr[e] - arr[s]
    if diff == m:
        answer = m
        break
    elif diff > m:
        answer = min(answer, diff)
        s += 1
    else:
        e += 1

print(answer)