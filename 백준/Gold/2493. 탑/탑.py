import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
ans = [0] * (N)
s = []
s.append(0) # index 푸시
for i in range(1, N):
    while s:
        if arr[s[-1]] >= arr[i]:
            ans[i] = s[-1] + 1
            break
        else:
            s.pop()
    s.append(i)  
for i in ans:
    print(ans[i], end = ' ')