def solution(s):
    answer = 1
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))] # 부분 문자열 dp[i..j] 에서 가장 긴 펠린드롬 길이
          
    for i in range(len(s)):
        dp[i][i] = 1
        
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = 1
            answer = 2
  
    for i in range(3, len(s)+1):
        for j in range(len(s)-i+1):
            e = j+i-1
            if dp[j+1][e-1] and s[j] == s[e]:
                dp[j][e] = 1
                answer = max(answer, i)
    return answer