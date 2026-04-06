import sys
input = sys.stdin.readline
n = int(input())
m = int(input())

parent = [i for i in range(n+1)] 

def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    pa, pb = find(a), find(b)
    if pa != pb:
        parent[pa] = pb

for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j]:
            union(i+1, j+1)
path = list(map(int, input().split()))
root = find(path[0])
print("YES" if all(find(p) == root for p in path) else "NO")
