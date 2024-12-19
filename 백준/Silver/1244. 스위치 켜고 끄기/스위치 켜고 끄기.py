import sys
input = sys.stdin.readline
N = int(input())
arr = [0] + list(map(int, input().split()))
S = int(input())

def toggle(n):
    if n == 0:
        return 1
    else:
        return 0

for i in range(S):
    s, n = map(int, input().split())
    if s == 1:
        for i in range(1, N+1):
            if i % n == 0:
                arr[i] = toggle(arr[i])
    elif s == 2:
        arr[n] = toggle(arr[n])
        for i in range(1, min(n, N-n+1)):
            if arr[n-i] == arr[n+i]:
                arr[n-i] = toggle(arr[n-i])
                arr[n+i] = toggle(arr[n+i])
            else:
                break
            
for i in range(1, len(arr)):
    print(arr[i], end = ' ')
    if i % 20 == 0:
        print()