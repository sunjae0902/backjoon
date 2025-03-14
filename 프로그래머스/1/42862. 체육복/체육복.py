def solution(n, lost, reserve):
    lost, reserve = set(lost) - set(reserve), set(reserve)-set(lost)
    for i in sorted(reserve):
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
    return n-len(lost)