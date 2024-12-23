import sys
input = sys.stdin.readline
arr = list(input().rstrip())
half = []
for i in range(arr.count('0') // 2):
    half.append(0)
for i in range(arr.count('1') // 2):
    half.append(1)
half.sort()
for i in half:
    print(i, end='')