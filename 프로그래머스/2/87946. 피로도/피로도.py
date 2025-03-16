from itertools import permutations
def solution(k, dungeons):
    answer = -1
    for perm in permutations(dungeons, len(dungeons)):
        cnt, cur = 0, k
        for dungeon in perm:
            if cur >= dungeon[0]:
                cur -= dungeon[1]
                cnt += 1
        answer = max(answer, cnt)
    return answer