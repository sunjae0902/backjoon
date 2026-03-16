import sys
input = sys.stdin.readline
n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
move = [(0,1), (0,-1), (-1, 0), (1, 0)] # 동 서 북 남
dir = list(map(int, input().split()))
dice = [0] * 6 # 위, 아래, 동 서 남 북

def turn(d):
    t, b, e, w, s, n = dice
    if d == 1: 
        dice[0], dice[1], dice[2], dice[3] = w, e, t, b
    elif d == 2:
        dice[0], dice[1], dice[2], dice[3] = e, w, b, t
    elif d == 4: # 남
        dice[0], dice[1], dice[4], dice[5] = n, s, t, b
    else:
        dice[0], dice[1], dice[4], dice[5] = s, n, b, t

for d in dir:
    nx, ny = x + move[d-1][0], y + move[d-1][1] # 이동 후 바닥면의 지도상 좌표
    if 0 <= nx < n and 0 <= ny < m:
        x, y = nx, ny
        turn(d)
        if board[x][y] == 0:
            board[x][y] = dice[1]
        else:
            dice[1] = board[x][y]
            board[x][y] = 0
        print(dice[0])
