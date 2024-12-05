import sys

input = sys.stdin.readline
N, K = map(int, input().split())

# 0-N까지의 정수를 K번 더해서 그 합이 N이 되는 경우의수 (중복해서 K개 뽑는다)


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fact(n - 1) * n


n = N + K - 1
r = N
ans = fact(n) // (fact(n - r) * fact(r))

print(ans % 1000000000)
