import sys
from collections import defaultdict
input = sys.stdin.readline
N, K = map(int, input().split())
arr = list(map(int, input().split()))
# dp = [{0:0} for _ in range(N)] # i번째 수열부터 포함했을 경우 같은 원소의 종류와 개수
# cnt = 0
# dp[0] = {arr[0]: 1}

# 시간 초과 (중복 검사 수행)
# for i in range(1,N):
#     sub = 0
#     for j in range(i, N):
#         val = dp[i].get(arr[j], 0)
#         if val + 1 <= K:
#             sub += 1
#             dp[i][arr[j]] = val + 1   
#         else:
#             break 
#     cnt = max(cnt, sub)
# print(cnt)

# 투 포인터
s, e, ans = 0, 0, 0
count = defaultdict(int) # s-e까지 포함했을 경우 같은 원소의 개수 저장
while e < N:
    if count[arr[e]] < K:
        count[arr[e]] += 1
        e += 1 # 다음 원소 탐색
        ans = max(ans, e-s)
    else:
        count[arr[s]] -= 1
        s += 1  # 시작 원소를 한 칸 당김
print(ans)