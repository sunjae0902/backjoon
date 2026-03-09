# 0 기둥
# 1 보

def possible_beam(x,y,s):
    if (x,y-1,0) in s or (x+1,y-1,0) in s:
        return True
    if (x-1, y, 1) in s and (x+1, y, 1) in s:
        return True
    return False

def possible_column(x,y,s):
    if y == 0:
        return True
    if (x-1,y,1) in s or (x,y,1) in s:
        return True
    if (x, y-1, 0) in s:
        return True
    return False

def possible(s):
    for x,y,a in s:
        if a:
            if not possible_beam(x,y,s):
                return False
        else:
            if not possible_column(x,y,s):
                return False
    return True

def solution(n, build_frame):
    answer = set()
    
    for x,y,a,b in build_frame:
        if b:
            answer.add((x,y,a))
            if not possible(answer):
                answer.remove((x,y,a))
        else:
            answer.remove((x,y,a))
            if not possible(answer):
                answer.add((x,y,a))
                
    answer = sorted(list(answer), key=lambda x: (x[0], x[1], x[2]))
    return answer