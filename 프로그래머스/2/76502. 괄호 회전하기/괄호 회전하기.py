def correct(arr):
    stack = []
    for s in arr:
        if s in '{([':
            stack.append(s)
        elif stack and ''.join([stack[-1], s]) in ['{}', '[]', '()']:
            stack.pop()
        else:
            return False
    if stack:
        return False
    return True     
    
def solution(s):
    answer = 0
    for i in range(len(s)):
        if correct(s[i:]+s[:i]):
            answer += 1
    return answer