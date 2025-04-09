def solution(a):
    answer = 2
    lmin = int(1e9)
    rmin = [a[-1]] 
    for i in range(len(a)-2, 1, -1): 
        rmin.append(min(rmin[len(a)-i-2], a[i]))
    rmin = rmin[::-1]
    
    for i in range(1, len(a)-1):
        lmin = min(lmin, a[i-1])
        if lmin < a[i] and a[i] > rmin[i-1]:
            continue
        answer += 1
        
    return answer