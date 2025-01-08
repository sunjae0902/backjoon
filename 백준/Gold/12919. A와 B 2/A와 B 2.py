import sys
from collections import deque
input = sys.stdin.readline
s = input().rstrip()
t = input().rstrip()
ans = 0
if s != t:
    q = deque([t])
    while q:
        now = q.popleft()
        if len(now) < len(s):
            break
        elif now == s:
            ans = 1
            break
        arr = []
        if now[-1] == 'A':
            arr.append(now[:len(now)-1])
        if now[0] == 'B':
            arr.append(''.join(list(reversed(now[1:]))))
        for item in arr:
            q.append(item)
print(ans)