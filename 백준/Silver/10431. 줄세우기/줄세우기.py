import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    cnt = 0 
    arr = list(map(int, input().split()))
    for i in range(1, 21):
        front = i
        for j in range(i-1, 0, -1):
            if arr[i] < arr[j]:
                front = j
        arr.insert(front, arr.pop(i))
        cnt += (i-front) 
    print(arr[0], end = ' ')
    print(cnt)