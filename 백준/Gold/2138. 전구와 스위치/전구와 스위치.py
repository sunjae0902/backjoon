import sys
input = sys.stdin.readline
N = int(input())
cur = list(map(int, input().rstrip()))
end = list(map(int, input().rstrip()))

def go(arr):
    count = 0
    for i in range(1, N-1):
        if end[i - 1] != arr[i - 1]:  # 무조건 옆의 스위치를 켜야 함
            count += 1
            for j in range(i-1, i+2):
                arr[j] ^= 1
    if end[N-1] != arr[N-1]:
        count += 1
        for j in range(N-2, N):
            arr[j] ^= 1
    if arr == end:
        return count
    else:
        return -1

if cur == end:
    print(0)
else:
    copied = cur.copy()
    copied[0] ^= 1
    copied[1] ^= 1
    # 0번 스위치를 누르는 경우, 누르지 않는 경우
    on = go(copied)
    cnt = [on+1 if on != -1 else -1]
    cnt.append(go(cur))
    if cnt[0] == cnt[1] == -1:
        print(-1)
    else:
        print(min([i for i in cnt if i != -1]))