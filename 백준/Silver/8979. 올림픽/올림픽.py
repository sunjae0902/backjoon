import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
rank = [0 for _ in range(N+1)] # i번 국가의 순서
for i in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(reverse=True, key = lambda x: (x[1], x[2], x[3]))

rank[arr[0][0]] = 1
cnt = 1
for i in range(1, len(arr)):
    if arr[i][1:] == arr[i-1][1:]:
        rank[arr[i][0]] = rank[arr[i-1][0]]
    else:
        rank[arr[i][0]] = cnt + 1     
    cnt += 1
print(rank[K])
    