def solution(n, s):
    answer = []
    if n <= s:
        if s % n == 0:
            answer = [s/n] * n
        else:
            rem = s % n
            answer = [s//n] * (n-rem) + [s//n+1] * (rem)
    return sorted(answer) if answer != [] else [-1]