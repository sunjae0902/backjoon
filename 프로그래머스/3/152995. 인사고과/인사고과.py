def solution(scores):
    answer = 0
    scores = [[i, score[0], score[1], 0] for i, score in enumerate(scores)]
    scores.sort(key=lambda x: (-x[1], x[2]))  # 점수1 내림차순, 점수2 오름차순

    tmp = set()
    max_b = -1
    for i in range(len(scores)):
        if scores[i][2] < max_b:
            tmp.add(scores[i][0])
        else:
            max_b = scores[i][2]

    if 0 in tmp:
        return -1
    rank = [score for score in scores if score[0] not in tmp]
    rank.sort(reverse=True, key= lambda x: x[1]+x[2])
    rank[0][3] = 1
    for i in range(1, len(rank)):
        if rank[i][1] + rank[i][2] == rank[i-1][1] + rank[i-1][2]:
            rank[i][3] = rank[i-1][3]
        else:
            rank[i][3] = i+1
    for i in range(len(rank)):
        if rank[i][0] == 0:
            answer = rank[i][3]
            break
    return answer 