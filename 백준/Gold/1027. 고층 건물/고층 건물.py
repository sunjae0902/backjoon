import sys
input = sys.stdin.readline

n = int(input())
height = list(map(int, input().split()))

def possible(c1, c2, c3):
    slope = (c1[1] - c2[1]) / (c1[0] - c2[0])
    y = c1[1] - slope * c1[0]
    if slope * c3[0] + y > c3[1]:
        return True
    return False                                                                                                                                                                            

cnt = [[] for _ in range(n)]

for i in range(n):
    c1 = (i, height[i])
    for j in range(i+1, n):
        c2 = (j, height[j])
        flag = 1
        for k in range(i+1, j):
            c3 = (k, height[k])
            if not possible(c1,c2,c3):
                flag = 0
                break
        if flag:
            cnt[i].append(j)
            cnt[j].append(i)
print(max(len(a) for a in cnt))
