import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
ref = Counter(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

for i in arr:
    print(ref[i], end= ' ')