import sys, math
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
total = int(input())
if sum(arr) <= total:
    print(max(arr))
else: 
    bound = 0
    def binary(start, end):
        while start <= end:
            mid = (start+end) // 2
            cnt = 0
            for i in range(len(arr)):
                cnt += min(arr[i], mid)
            if total >= cnt:
                start = mid + 1
            else:
                end = mid - 1
        return end
    bound = binary(math.trunc(total/N)-1, max(arr))
    print(bound)