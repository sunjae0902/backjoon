import sys, heapq
input = sys.stdin.readline
N = int(input())
hq = []
# 우선순위 큐, (각 열이 정렬됨, 큐 사이즈 유지하며 비교하기)

for i in range(N):
    arr = list(map(int, input().split())) 
    if i == 0:
        for j in arr:
            heapq.heappush(hq, j)
        continue
    for j in arr:
        if len(hq) < N:
            heapq.heappush(hq, j)
        # hq[0]: 루트 노드 확인하기
        elif hq[0] < j: # 큐의 최솟값보다 크면 푸시.
            heapq.heappush(hq, j) # 정렬 유지
            heapq.heappop(hq)
print(heapq.heappop(hq))
