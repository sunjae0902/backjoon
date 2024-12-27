import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
# 키가 1,2,, N인 사람들이 왼쪽에 큰 사람이 몇명있는지 기억함
ans = [0] * N
for i in range(N):
    cnt = 0
    # 각 자리 수 만큼 채워준다
    for j in range(N):
        if cnt == arr[i] and ans[j] == 0:
            ans[j] = i+1
            break
        elif ans[j] == 0:
            cnt += 1
print(' '.join(map(str, ans)))