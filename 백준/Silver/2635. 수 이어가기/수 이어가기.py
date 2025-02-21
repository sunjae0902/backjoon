import sys
input = sys.stdin.readline
N = int(input())
answer = []
for i in range(1, N + 1):
    arr = [N, i]
    j = len(arr)
    while arr[j - 2] - arr[j - 1] >= 0:
        arr.append(arr[j - 2] - arr[j - 1])
        j += 1
    if len(answer) < len(arr):
        answer = arr
print(len(answer))
for i in answer:
    print(i, end=" ")