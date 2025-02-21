import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))

def bn_search(arr, key):
    s, e = 0, len(arr)-1
    while s <= e:
        m = (s+e) // 2
        if arr[m] == key:
            return 1
        elif arr[m] > key:
            e = m - 1
        else:
            s = m + 1
    return 0
arr.sort()
for n in num:
    if n < arr[0] or n > arr[-1]:
        print(0)
        continue
    print(bn_search(arr, n))