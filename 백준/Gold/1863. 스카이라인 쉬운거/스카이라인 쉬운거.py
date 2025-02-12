import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0
s = []
for i in range(N):
    height = arr[i][1]
    while s and s[-1] > height:
        s.pop()
    if not s or s[-1] < height:
        s.append(height)
        if height > 0:
            answer += 1
print(answer)