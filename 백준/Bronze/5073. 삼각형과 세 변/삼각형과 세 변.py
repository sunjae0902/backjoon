import sys
input = sys.stdin.readline

while True:
    arr = list(map(int, input().split()))
    slen = len(set(arr))
    arr.sort()
    if arr == [0,0,0]:
        break
    elif slen == 1:
        print("Equilateral")
    elif arr[-1] >= arr[0] + arr[1]:
        print("Invalid")
    elif slen == 2:
        print("Isosceles")
    elif slen == 3:
        print("Scalene")
