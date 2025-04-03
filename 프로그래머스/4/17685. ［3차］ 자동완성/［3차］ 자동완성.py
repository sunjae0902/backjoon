def solution(words):
    answer = [0] * len(words)
    words.sort()
    
    for i in range(len(words)-1):
        a, b = len(words[i]), len(words[i+1])
        for j in range(min(a, b)):
            if words[i][j] != words[i+1][j]: # 불일치
                j -= 1 # 마지막으로 일치하는 자리
                break

        answer[i] = max(answer[i], min(j+2, a))
        answer[i+1] = max(answer[i+1], min(j+2, b))
        
    return sum(answer)
