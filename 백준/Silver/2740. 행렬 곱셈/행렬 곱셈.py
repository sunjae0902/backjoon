import sys
input = sys.stdin.readline

a1 = []
a2 = []
N,M = map(int, input().split())
a1 = [list(map(int, input().split())) for _ in range(N)]
# for i in range(N):
#     a1.append(list(map(int, input().split())))
M,K = map(int, input().split())
a2 = [list(map(int, input().split())) for _ in range(M)]
# for i in range(N):
#     a2.append(list(map(int, input().split())))
    
res = [[0] * K for _ in range(N)]

for i in range(N): # a1의 행
    for j in range(K): # a2의 열
        tmp = 0
        for k in range(M): # a1의 열, a2의 행
            tmp += a1[i][k] * a2[k][j]
        res[i][j] = tmp
        
for i in res:
    for j in i:
        print(j, end=' ')
    print()