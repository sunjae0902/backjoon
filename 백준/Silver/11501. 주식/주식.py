import sys
input = sys.stdin.readline
T = int(input())
# 뒤에서부터 최댓값을 탐색하여 시간 복잡도 줄이기
for _ in range(T):
    total = 0
    N = int(input())
    coin = list(map(int, input().split()))

    max_val = 0  # 현재까지의 최대값
    for c in coin[::-1]:  # 뒤에서부터 탐색
        if c > max_val:
            max_val = c  # 최대값 갱신
        total += max_val - c
    print(total)
