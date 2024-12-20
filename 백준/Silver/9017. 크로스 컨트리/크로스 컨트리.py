import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    arr = [[] for _ in range(201)]
    tmp = list(map(int, input().split()))
    cnt = 1
    for i in range(len(tmp)):
        if tmp.count(tmp[i]) >= 6:
            arr[tmp[i]].append(cnt)
            cnt += 1
    tmp = []
    for i in range(len(arr)):
        if len(arr[i]) > 0:
            tmp.append([i, sum(arr[i][:4]), sum(arr[i][:5]), sum(arr[i])])
    tmp.sort(key= lambda x: (x[1], x[2], x[3]))
    print(tmp[0][0])