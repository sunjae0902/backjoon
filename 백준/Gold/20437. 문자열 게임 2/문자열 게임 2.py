import sys
from collections import defaultdict
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    w = input().rstrip()
    k = int(input())
    ans1, ans2 = len(w)+1, k-1
    cnt = defaultdict(list)
    for i in range(len(w)):
        cnt[w[i]].append(i)

    for key, val in cnt.items():
        if len(val) >= k:
            for i in range(len(val)-k+1):
                ans1 = min(ans1, cnt[key][i:i+k][-1] - cnt[key][i:i+k][0]+1)
                if w[cnt[key][i:i+k][-1]] == w[cnt[key][i:i+k][0]]:
                    ans2 = max(ans2, cnt[key][i : i + k][-1] - cnt[key][i : i + k][0] + 1)
    if ans1 == len(w)+1 or ans2 == k-1:
        print(-1)
    else:
        print(ans1, ans2)