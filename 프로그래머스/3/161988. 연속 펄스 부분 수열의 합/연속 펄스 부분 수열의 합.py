def solution(sequence):
    answer = [0, 0]
    n = len(sequence)
    
    pulse = [[], []]
    for i in range(n):
        if i % 2 == 0:
            pulse[0].append(-sequence[i])
            pulse[1].append(sequence[i])
        else:
            pulse[0].append(sequence[i])
            pulse[1].append(-sequence[i])
            
    for i in range(2):
        dp = [0] * len(pulse[i])
        dp[0] = pulse[i][0]
        for j in range(1, len(pulse[i])):
            dp[j] = max(pulse[i][j], dp[j-1] + pulse[i][j])
        answer[i] = max(dp)
    return max(answer)