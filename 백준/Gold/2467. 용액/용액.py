import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 0에 가장 가깝다 -> 합의 절댓값이 최소다.

# 각 요소를 순회하면서, i+1 ~ N-1 번째 요소의 합 중 최소가 되는 경우를 이진 탐색으로 구한다.
# 시간 복잡도 nlogn
min = float("INF")
a, b = 0, 0
for i in range(N):
    cur = arr[i] # 기준점
    start = i + 1
    end = N - 1
    while(start <= end):
        mid = (start + end) // 2
        # 최솟값을 구하는 로직
        if abs(cur + arr[mid]) < min:
            min = abs(cur + arr[mid])
            a, b = cur, arr[mid]
        # 탐색 범위를 업데이트하는 로직(음수일 경우, arr[mid]가 커져야 0에 가까워짐, 양수일땐 반대)
        if cur + arr[mid] < 0:
            start = mid + 1
        else:
            end = mid - 1
print(a,b) 