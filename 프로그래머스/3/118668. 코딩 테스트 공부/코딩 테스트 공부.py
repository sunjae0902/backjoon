def solution(alp, cop, problems):
    answer = 0
    alp_max, cop_max = max([i[0] for i in problems]), max([i[1] for i in problems])
    alp = min(alp, alp_max)
    cop = min(cop, cop_max)
    dp = [[int(1e9) for _ in range(cop_max+2)] for _ in range(alp_max+2)]
    dp[alp][cop] = 0
    
    for a in range(alp, alp_max+1):
        for c in range(cop, cop_max+1):
            dp[a+1][c] = min(dp[a+1][c], dp[a][c] + 1) # 알고력 공부
            dp[a][c+1] = min(dp[a][c+1], dp[a][c] + 1) # 코딩력 공부
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:
                    alp_new, cop_new = min(alp_max, a+alp_rwd), min(cop_max, c+cop_rwd)
                    dp[alp_new][cop_new] = min(dp[alp_new][cop_new], dp[a][c] + cost)
    return dp[alp_max][cop_max]