import sys
input = sys.stdin.readline
N, M = map(int, input().split())
keyword = set([input().rstrip() for _ in range(N)])

for i in range(M):
    new_keyword = list(map(str, input().rstrip().split(",")))
    for nk in new_keyword:
        if nk in keyword:
            keyword.remove(nk)
    print(len(keyword))