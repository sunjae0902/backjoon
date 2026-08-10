def solution(n):
    answer = 0
    board = [-1] * n # i번째 행의 board[i]번째 열에 배치

    def dfs(row): # row 행에 배치할게
        nonlocal answer

        if row == n:
            answer += 1 # 가능
            return

        for col in range(n):
            # 같은 열에 퀸이 있는지
            for prev_row in range(row):
                prev_col = board[prev_row]

                # 같은 열
                if prev_col == col:
                    break

                # 대각선
                if abs(prev_row - row) == abs(prev_col - col):
                    break
            else:
                board[row] = col
                dfs(row + 1)
                board[row] = -1

    dfs(0)
    return answer