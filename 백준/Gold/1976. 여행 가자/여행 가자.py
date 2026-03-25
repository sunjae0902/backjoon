import sys
input = sys.stdin.readline
from collections import deque

n = int(input()) # 도시 수 
m = int(input()) # 여행 계획 도시 수
graph = [[] for _ in range(n+1)]
parent = [i for i in range(n + 1)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    pa, pb = find(a), find(b)
    if pa != pb:
        parent[pa] = pb

for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    for j in range(1, n+1):
        if tmp[j-1] == 1: # 연결
            union(i, j)
            
travel = deque(list(map(int, input().split())))
root = find(travel[0])

print("YES" if all(find(parent[n]) == root for n in travel) else "NO") 
