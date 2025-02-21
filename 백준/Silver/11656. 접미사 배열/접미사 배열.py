import sys
input = sys.stdin.readline
st = input().rstrip()
arr = []
for i in range(len(st)):
    arr.append(st[i:])
arr.sort()
for i in arr:
    print(i)