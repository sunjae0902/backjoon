import sys
input = sys.stdin.readline
s = 0
visited = set()
n = int(input())
answer = 0
arr = list(map(int, input().split()))
for e in range(n):
    while arr[e] in visited:
        visited.remove(arr[s])
        s += 1
    visited.add(arr[e])
    answer += (e-s+1) # e번째 수가 추가되면서 증가한 부분수열 갯수 상수화
print(answer)