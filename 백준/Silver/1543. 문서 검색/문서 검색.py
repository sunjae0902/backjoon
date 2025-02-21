import sys
input = sys.stdin.readline
doc = input().rstrip()
target = input().rstrip()
answer = 0
last = -1
for i in range(len(doc)-len(target)+1):
    if target == doc[i:i+len(target)] and last < i:
        answer += 1
        last = i + len(target) - 1
print(answer)