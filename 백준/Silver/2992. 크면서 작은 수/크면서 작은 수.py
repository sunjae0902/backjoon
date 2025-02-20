import sys
from itertools import permutations

input = sys.stdin.readline
narr = list(input().rstrip())
num = int("".join(narr))
arr = []
for p in permutations(narr):
    arr.append(int("".join(p)))
arr.sort()
for i in range(len(arr)):
    if arr[-1] == num:
        print(0)
        break
    if arr[i] == num and arr[i+1] != num:
        print(arr[i + 1])
        break