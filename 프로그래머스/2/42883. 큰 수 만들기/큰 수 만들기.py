def solution(number, k):
    stack = []
    for j in range(len(number)):
        while k > 0 and stack and int(stack[-1]) < int(number[j]): # 작은 값이 있으면 뺀다
            k -= 1
            stack.pop()
        stack.append(number[j]) 
    return ''.join(stack[:len(number)-k]) if len(set(list(number))) != 1 else number[:len(number)-k]
