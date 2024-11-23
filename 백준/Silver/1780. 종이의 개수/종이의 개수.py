import sys
input = sys.stdin.readline
N = int(input())
arr = []
f = 0
s = 0
t = 0
def isSame(arr):
    val = arr[0][0]
    for i in arr:
        for j in i:
            if j != val:
                return False
    return True

def recur(arr):
    global f,s,t
    if isSame(arr):
        if arr[0][0] == -1:
            f += 1
        elif arr[0][0] == 0:
            s += 1
        elif arr[0][0] == 1:
            t += 1
    else:
        l = len(arr)
        for i in range(3):
            for j in range(3):
                recur([row[j * l // 3:(j + 1) * l // 3] for row in arr[i * l // 3:(i + 1) * l // 3]])
for i in range(N):
    arr.append(list(map(int, input().strip().split())))

recur(arr)
print(f)
print(s)
print(t)