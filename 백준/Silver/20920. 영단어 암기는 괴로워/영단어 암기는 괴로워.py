import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dict = {}
for i in range(N):
    s = input().rstrip()
    if len(s) >= M:
        if s in dict:
            dict[s] += 1
        else:
            dict[s] = 1
words = sorted(dict.items(), key = lambda x:(-x[1], -len(x[0]), x[0]))
for w in words:
    print(w[0])
