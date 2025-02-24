import sys
input = sys.stdin.readline
N = int(input())
answer = int(1e9)
for i in range(N//5+1):
    rem = N - i * 5
    if rem % 2 == 0:
        answer = min(answer, rem//2 + i)
print(answer if answer != int(1e9) else -1)