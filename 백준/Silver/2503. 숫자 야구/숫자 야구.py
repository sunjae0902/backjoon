import sys
from itertools import permutations
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
answer = 0

def strike(n1, n2):
    count = 0
    for i in range(len(n1)):
        if n1[i] == n2[i]:
            count += 1
    return count

def bol(n1, n2):
    return len(set(n1).intersection(set(n2))) - strike(n1, n2)

for perm in permutations([i for i in range(1, 10)], 3):
    perm = list(perm)
    flag = 1
    for i in range(N):
        target =  list(map(int, str(arr[i][0])))
        if strike(perm, target) != arr[i][1] or bol(perm, target) != arr[i][2]:
            flag = 0
            break
    if flag:
        answer += 1
print(answer)