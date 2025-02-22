import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    s = list(input().rstrip())
    e = list(input().rstrip())
    dif = []
    for j in range(N):
        if s[j] != e[j]:
            dif.append(s[j])
    cnt_w, cnt_b = dif.count('W'), dif.count('B')
    if cnt_w != 0 and cnt_b != 0:
        pair = min(cnt_w, cnt_b)
        print(len(dif)-pair)
    else:
        print(cnt_w if cnt_w != 0 else cnt_b)