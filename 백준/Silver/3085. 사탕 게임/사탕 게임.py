import sys
input = sys.stdin.readline
N = int(input())
arr = [[0 for j in range(N)] for i in range(N)]
cnt = 0

for i in range(N):
    s = input().rstrip()
    for j in range(N):
        arr[i][j] = s[j]

def count(arr):
    maxCountRow, maxCountCol = 0, 0
    for i in range(N):
        tmp = 0
        for j in range(N-1):
            if arr[i][j] == arr[i][j+1]:
                tmp += 1
            else:
                tmp = 0
            maxCountRow = max(maxCountRow, tmp+1)
    
        tmp = 0
        for j in range(N-1):
            if arr[j][i] == arr[j+1][i]:
                tmp += 1
            else:
                tmp = 0
            maxCountCol = max(maxCountCol, tmp+1)
    return max(maxCountCol, maxCountRow)


for i in range(N):
    for j in range(N):
        if j < N-1:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            cnt = max(cnt,count(arr))
            
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
        if i < N-1:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            cnt = max(cnt, count(arr))
            
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
print(cnt)