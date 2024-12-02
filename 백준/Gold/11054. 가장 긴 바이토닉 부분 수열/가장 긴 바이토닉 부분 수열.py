import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
inc = [1] * N # 왼쪽에서부터 arr[i]를 마지막으로 하는 증가하는 부분수열 최대길이 저장,
dec = [1] * N # 오른쪽에서부터 arr[i]를 마지막으로 하는 증가하는 부분수열 최대길이 저장

for i in range(N):
    last_inc = arr[i]
    for j in range(i):
        if arr[j] < last_inc: # 오름
            inc[i] = max(inc[i], inc[j]+1)
            
for i in range(N-1, -1, -1):
    last_dec = arr[i]
    for j in range(N-1, i, -1):
        if arr[j] < last_dec: # 역순으로 오름차순
            dec[i] = max(dec[i], dec[j]+1)

            
res = [0 for _ in range(N)]
for i in range(N):
    res[i] = inc[i] + dec[i] -1
print(max(res))