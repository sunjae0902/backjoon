import sys
input = sys.stdin.readline
N = int(input())
arr = sorted(list(map(int, input().split())))
cnt = 0
for i in range(N): # 주의, 숫자가 같더라도 위치가 다르면 다른 숫자임
    cur = arr[i]
    flag = 0
    start = 0 # 기준값도 포함된 전체 배열 탐색. 
    end = N - 1
    while start < end:
        if start == i: # 자기 자신인 경우 제외
            start += 1
            continue
        if end == i:
            end -= 1
            continue
        if cur == arr[start] + arr[end]:
            flag = 1
            break
        elif cur < arr[start] + arr[end]: # 기준 값이 더 작은 경우, 큰 포인터를 줄여야함
            end -= 1
        else:
            start += 1
    if flag == 1:
        cnt += 1
print(cnt)