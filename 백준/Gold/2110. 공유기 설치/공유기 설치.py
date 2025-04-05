import sys
input = sys.stdin.readline
N, C = map(int, input().split())
loc = [int(input()) for _ in range(N)]
loc.sort()
answer = 0
s, e = 1, loc[-1]-loc[0] # 공유기 거리 탐색 범위

while s <= e:
    m = (s+e)//2 # 현재 가장 가까운 두 공유기 거리
    count = 1
    idx = 0
    for i in range(len(loc)): # 설치 가능한 범위
        if loc[i] >= loc[idx] + m:
            idx = i
            count += 1
    if count < C: # 목표보다 작다 -> 공유기 사이 거리를 줄인다
        e = m - 1
    else:
        s = m + 1
        answer = m  # 목표보다 크다 -> 공유기 사이 거리를 늘린다
print(answer)