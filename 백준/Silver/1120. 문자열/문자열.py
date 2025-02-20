import sys
input = sys.stdin.readline
a, b = input().split()
# 슬라이딩 윈도우
res = len(b)

for i in range(len(b) - len(a) + 1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt += 1
    res = min(res, cnt)
print(res)