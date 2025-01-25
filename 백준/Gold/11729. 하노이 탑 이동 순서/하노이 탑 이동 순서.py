import sys
input = sys.stdin.readline
N = int(input())
arr = []

def hanoi(s, e, n): # 1 3 3
    if n == 1:
        arr.append([s,e])
        return
    hanoi(s, 6-s-e, n-1)
    hanoi(s, e, 1)
    hanoi(6-s-e, e, n-1)
    
hanoi(1,3,N)
print(len(arr))
for i in arr:
    print(i[0], i[1])