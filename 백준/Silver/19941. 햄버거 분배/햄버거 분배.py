import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(input().rstrip())
cnt = 0
# 방향성이 있다. 왼쪽부터 먹어야 오른쪽 사람들 선택지가 늘어남 ->  왼쪽부터 순방향 for문이 더 낫다.
for i in range(len(arr)):
    if arr[i] == 'P':
        for j in range(max(0, i-K), min(N,i+K+1)):
            if arr[j] == 'H':
                arr[j] = '-'
                cnt += 1
                break     # 하나 먹으면 바로 break       
print(cnt)
