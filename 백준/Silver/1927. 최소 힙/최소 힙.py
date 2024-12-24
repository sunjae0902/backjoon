import sys, heapq
input = sys.stdin.readline
hq = []
N = int(input())
for i in range(N):
    n = int(input())
    if n == 0:
        if hq == []:
            print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, n)