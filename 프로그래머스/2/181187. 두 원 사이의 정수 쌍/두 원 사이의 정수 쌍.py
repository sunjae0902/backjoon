import math
def solution(r1, r2):
    answer = (r2-r1+1)
    for x in range(1, r2): 
        maxy = math.floor(math.sqrt((r2**2-x**2))) 
        miny = math.ceil(math.sqrt((r1**2-x**2))) if x < r1 else 0 
        if miny != 0:
            answer += (maxy-miny+1)
        else:
            answer += maxy-miny
    return 4 * answer