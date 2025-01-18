def solution(dirs):
    answer = 0
    s = (0,0) 
    visited = set()
    dir = {'L': [-1, 0], 'R': [1, 0], 'U': [0, 1], 'D': [0, -1]}
    for d in list(dirs):
        e = (dir[d][0] + s[0], dir[d][1] + s[1])
        if -5 <= e[0] <= 5 and -5 <= e[1] <= 5:
            visited.add((s[0], s[1], e[0], e[1])) # 두 방법은 하나로 간주함
            visited.add((e[0], e[1], s[0], s[1]))
            s = e
    answer = len(visited) // 2
    return answer