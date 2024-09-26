import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    arr = []
    for j in range(N):
        a,b = map(int, input().strip().split())
        arr.append([a,b])
    arr.sort()
    first = arr[0][0]
    second = arr[0][1]
    max = 1
    for j in range(1,N):
        if arr[j][0] > first and arr[j][1] > second:
            continue
        else:
            if arr[j][0] <= first:
                first = arr[j][0]
            if arr[j][1] <= second:
                second = arr[j][1]
            max += 1    
    print(max)
        