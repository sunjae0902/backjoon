from collections import deque
def possible(w1, w2):
    for i in range(len(w1)):
        removed_1 = w1[:i] + w1[i+1:]
        removed_2 = w2[:i] + w2[i+1:]
        if removed_1 == removed_2:
            return True
    return False

def solution(begin, target, words):
    answer = len(words)
    # 하나만 바꾼게 words에 있어야 함 
    if target not in words:
        return 0
    
    q = deque([(begin, 0)])
    visited = set()
    while q:
        cur_word, depth = q.popleft()
        if cur_word == target:
            answer = min(answer, depth)
        for w in words:
            if w not in visited and possible(cur_word, w):
                visited.add(w)
                q.append((w, depth+1))             
    return answer