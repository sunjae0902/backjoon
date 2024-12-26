import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: x[0])
ans = 0
height = 0
max_height = 0
idx = 0
for i in range(len(arr)):
    if arr[i][1] > max_height:
        max_height = arr[i][1]
        idx = i

for i in range(len(arr[:idx+1])):
    if height < arr[i][1]:
        height = arr[i][1]
    if i < len(arr[:idx+1])-1:
        for j in range(arr[i][0], arr[i+1][0]):
            ans += height
    else:
        ans += height
height = 0
for i in range(N-1, idx, -1):
    if height < arr[i][1]:
        height = arr[i][1]
    for j in range(arr[i][0], arr[i-1][0], -1):
         ans += height
print(ans)