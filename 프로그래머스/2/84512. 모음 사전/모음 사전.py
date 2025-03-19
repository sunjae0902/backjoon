from itertools import product

def solution(word):
    answer = 0
    words = []
    for i in range(1,6):
        for p in product(['A', 'E', 'I', 'O', 'U'], repeat = i):
            words.append(''.join(list(p)))
    answer = sorted(words).index(word)+1
    return answer