import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
arr = [(0, i) for i in arr]

while True:
    if [i[1] for i in arr].count(0) >= K:
        break
    # 벨트 회전
    arr.insert(0, arr[-1])
    arr.pop()
    # 내림
    if arr[N - 1][0]:
        arr[N - 1] = (0, arr[N - 1][1])
    # 로봇 이동
    for i in range(N-2, -1, -1):
        if arr[i][0] and not arr[i+1][0] and arr[i+1][1] >= 1:
            arr[i+1] = (1, arr[i+1][1]-1)
            arr[i] = (0, arr[i][1])
    # 내림
    if arr[N-1][0]:
        arr[N-1] = (0, arr[N-1][1])
    # 올림
    if not arr[0][0] and arr[0][1] >= 1:
        arr[0] = (1, arr[0][1] - 1)
    cnt += 1
print(cnt)