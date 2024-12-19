import sys
input = sys.stdin.readline

N, score, p = map(int, input().split())
arr = list(map(int, input().split()))
res = 1
if len(arr) >= p and min(arr) >= score:
    res = -1
else:
    arr.append(score)
    arr.sort(reverse=True)
    for i in range(len(arr)-1):
        if arr[i] == score:
            break
        res += 1
print(res)