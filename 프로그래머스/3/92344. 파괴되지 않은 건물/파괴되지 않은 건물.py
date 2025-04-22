def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    prefix = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for t, r1, c1, r2, c2, d in skill:
        prefix[r1][c1] += -d if t == 1 else d
        prefix[r2+1][c2+1] += -d if t == 1 else d
        prefix[r1][c2+1] += d if t == 1 else -d
        prefix[r2+1][c1] += d if t == 1 else -d
        
    for i in range(n): #행
        for j in range(m):
            prefix[i+1][j] += prefix[i][j]
            
    for i in range(m): #열
        for j in range(n):
            prefix[j][i+1] += prefix[j][i]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] + prefix[i][j] > 0:
                answer += 1
    return answer