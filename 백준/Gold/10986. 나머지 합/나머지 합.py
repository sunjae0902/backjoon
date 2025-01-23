# 누적 합, 나머지 계산, 조합 문제
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
prefix = [0] * (N+1)
for i in range(N):
    prefix[i+1] = prefix[i] + arr[i]
mod_cnt = [0] * M # 누적합의 차이(구간합)가 M으로 나누어 떨어진다는 것은, 두 누적합을 M으로 나눈 나머지가 같음을 의미
ans = 0
for p in prefix:
    mod = p % M 
    ans += mod_cnt[mod] 
    mod_cnt[mod] += 1
print(ans)