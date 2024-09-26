import sys
input = sys.stdin.readline
N = int(input())
arr = [[0] * N] * N

ws = 0
bs = 0

def isSameColor(arr):
    val = arr[0][0]
    for i in arr:
        for j in i:
            if j != val:
                return False
            continue
    return True

def recur(arr):
    global ws,bs
    if isSameColor(arr):
        if arr[0][0] == 0:
            ws += 1 
        else:
            bs += 1 
        return 
    else:
        l = len(arr)
        for i in range(2):
            for j in range(2):
                recur([row[j * l // 2:(j + 1) * l // 2] for row in arr[i * l // 2:(i + 1) * l // 2]])

for i in range(N):
    arr[i] = list(map(int, input().strip().split()))
    
recur(arr)
print(ws)
print(bs)