import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict = {}
for i in range(N):
    name, score = map(str, input().split())
    if dict.get(score):
        continue
    dict[score] = name 
def bs(key, arr):
    s, e, res = 0, len(arr)-1, 0
    while s <= e:
        m = (s+e) // 2
        if arr[m] < key:
            s = m + 1
        else:
            e = m - 1
            res = m
    return arr[res]
keys = list(map(int, dict.keys()))
for i in range(M):
    c = int(input())
    key = bs(c, keys)
    print(dict[str(key)])