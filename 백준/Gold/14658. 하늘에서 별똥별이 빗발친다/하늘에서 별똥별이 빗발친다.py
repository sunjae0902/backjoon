import sys
input = sys.stdin.readline

n,m,l,k = map(int, input().split())
cd = [list(map(int, input().split())) for _ in range(k)]

def cnt(org_x, org_y): # 부딪히는 별 개수
    res = k
    for x, y in cd:
        if (org_x <= x <= org_x + l) and (org_y <= y <= org_y + l):
            res -= 1
    return res

res = k
for x, _ in cd:
    for _, y in cd:
        res = min(res, cnt(x, y))
print(res)