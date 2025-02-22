import sys
from collections import defaultdict

input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
answer = []
hamming_cnt = 0
for i in range(M):
    neu = defaultdict(int)
    for j in range(N):
        neu[arr[j][i]] += 1
    keys = [k for k, v in neu.items() if max(neu.values()) == v]
    keys.sort()
    answer.append(keys[0])
    for j in range(N):
        if keys[0] != arr[j][i]:
            hamming_cnt += 1
print("".join(answer))
print(hamming_cnt)
