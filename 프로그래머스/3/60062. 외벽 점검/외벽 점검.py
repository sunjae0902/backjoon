from itertools import permutations
        
def solution(n, weak, dist):
    answer = len(dist)+1
    weak += [w + n for w in weak]

    for i in range(1, len(dist)+1):
        for perm in permutations(dist, i):
            for start in range(len(weak)//2): # 취약 지점에서 출발
                count = 0
                pos = weak[start] + perm[count]
                
                for idx in range(start, start + len(weak) // 2):
                    if weak[idx] > pos:
                        count += 1
                        if count >= i:
                            break
                        pos = weak[idx] + perm[count]
                else:
                    answer = min(answer, i)  
                               
    return answer if answer <= len(dist) else -1