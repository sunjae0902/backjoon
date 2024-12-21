import sys, math
input = sys.stdin.readline

N = int(input())
M = int(input())
pos = list(map(int, input().split()))
height = 0
maxdif = 0
for i in range(len(pos)-1):
    maxdif = max(maxdif, math.ceil((pos[i+1]-pos[i]) / 2))
for i in range(max(pos[0], N-pos[-1]), N+1):
    if i >= maxdif:
        height = i
        break  
print(height)