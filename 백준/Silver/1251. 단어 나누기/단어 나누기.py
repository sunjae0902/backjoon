import sys
from itertools import combinations
input = sys.stdin.readline
arr = list(input().rstrip())
answer = []
for comb in combinations([i for i in range(len(arr))], 2):
    comb = list(comb)
    f, s, t = arr[: comb[0]+1][::-1], arr[comb[0]+1 : comb[1]+1][::-1], arr[comb[1] + 1:][::-1]
    if len(f) < 1 or len(s) < 1 or len(t) < 1:
        continue
    answer.append(f+s+t)
print(''.join(sorted(answer)[0]))