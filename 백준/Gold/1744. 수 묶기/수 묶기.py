import sys
input = sys.stdin.readline
N = int(input())
pos = []
min = []
for i in range(N):
    a = int(input())
    if a > 0:
        pos.append(a)
    else:
        min.append(a)
pos.sort(reverse=True) # 내림 차순
min.sort() # 오름 차순
sum = 0

if N == 1:
    sum = pos[0] if len(pos) == 1 else min[0]
else:
    i,j = 0,0
    while i < len(pos): 
        if i < len(pos)-1 and pos[i] * pos[i+1] > pos[i] + pos[i+1]:
            sum += pos[i] * pos[i+1]
            i += 2
        else:
            sum += pos[i]
            i += 1
    while j < len(min):
        if j < len(min)-1:
            sum += min[j] * min[j+1]
            j += 2
        else:
            sum += min[j]  
            j += 1 
print(sum)