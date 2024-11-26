import sys, heapq
input = sys.stdin.readline
arr = []
heap = []

N = int(input())
for i in range(N):
    s,t = map(int, input().split())
    arr.append([s,t])

arr.sort(key = lambda x: (x[0], x[1])) 
heapq.heappush(heap, arr[0][1]) 

for i in range(1, N):
    if arr[i][0] < heap[0]:
        heapq.heappush(heap, arr[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, arr[i][1])
print(len(heap))