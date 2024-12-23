import sys
input = sys.stdin.readline
N = int(input())
arr = [input().rstrip() for _ in range(N)]
ans = 0
# 하나씩 지워가며 비교하기
for i in range(1, len(arr)):
    target = list(arr[0])
    cnt = 0
    for j in arr[i]:
        if j in target:
            target.remove(j)
        else:
            cnt += 1
    if cnt < 2 and len(target) < 2:
        ans += 1     
print(ans)