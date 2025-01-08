import sys
from collections import deque
input = sys.stdin.readline
s = input().rstrip()
t = input().rstrip()
ans = 0
def recur(start):
    if len(start) < len(s):
        return 0
    elif start == s:
        return 1
    else:
        ans1, ans2 = 0, 0
        if start[-1] == 'A':
            ans1 = recur(start[:len(start)-1])
        if start[0] == 'B':
            ans2 = recur(''.join(list(reversed(start[1:]))))
        return ans1 or ans2
ans = recur(t)
print(ans)