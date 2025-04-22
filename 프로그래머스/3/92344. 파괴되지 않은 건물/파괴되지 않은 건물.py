def solution(board, skill):
    answer = 0
    N, M = len(board), len(board[0])
    prefix_sum = [[0 for _ in range(M+1)] for _ in range(N+1)]
    
    for t, r1, c1, r2, c2, d in skill:
        prefix_sum[r1][c1] += -d if t == 1 else d
        prefix_sum[r1][c2+1] += d if t == 1 else -d
        prefix_sum[r2+1][c1] += d if t == 1 else -d
        prefix_sum[r2+1][c2+1] += -d if t == 1 else d
        
    # 행 누적합
    for i in range(N):
        for j in range(M):
            prefix_sum[i][j+1] += prefix_sum[i][j]
    # 열 누적합
    for j in range(M):
        for i in range(N):
            prefix_sum[i+1][j] += prefix_sum[i][j]
            
    for i in range(N):
        for j in range(M):
            if board[i][j] + prefix_sum[i][j] > 0:
                answer += 1
              
    return answer