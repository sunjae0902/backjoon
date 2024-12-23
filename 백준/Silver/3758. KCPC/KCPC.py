import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    n, k, t, m = map(int, input().split())
    log = [list(map(int, input().split())) for _ in range(m)]
    # 점수 높음 -> 횟수 적음 -> 마지막 제출 빠름(적)
    # 팀의 등수가 높은대로 저장
    # id 총점 횟수 인덱스(마지막 제출)
    rank = [[i, 0, 0, 0] for i in range(n+1)]
    tmp = [[0 for _ in range(k+1)] for _ in range(n+1)] 
    for i in range(len(log)):
        team, num, score = log[i][0], log[i][1], log[i][2]
        tmp[team][num] = max(tmp[team][num], score)
        rank[team][2] += 1
        rank[team][3] = i
    for i in range(1,n+1):
        rank[i][1] = sum(tmp[i])
    rank.remove(rank[0])
    rank.sort(reverse=True, key = lambda x: (x[1], -x[2], -x[3]))
    for r in range(len(rank)):
        if rank[r][0] == t:
            print(r+1)
            break