import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

def binarySearch(start, end):
    while(start <= end):
        mid = (start + end) // 2
        tmp = 0
        for i in range(N):
            if tree[i] > mid:
                tmp += tree[i] - mid
        if tmp >= M:
            start = mid + 1
        else:
            end = mid -1
    return end
            
max = binarySearch(0, max(tree))
print(max)  