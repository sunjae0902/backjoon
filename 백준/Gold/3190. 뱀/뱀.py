import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
move = [(0,1), (1,0), (0,-1), (-1,0)] # 오른쪽, 아래, 왼쪽, 위 (시계방향 90도 회전 순서)
board = [[0] * n for _ in range(n)]

for _ in range(k):
    i, j = map(int, input().split())
    board[i-1][j-1] = 1

l = int(input())
rotate = {}
for _ in range(l): # s초에 d방향
    s, d = input().split()
    rotate[int(s)] = d

sec = 0
dir_idx = 0
snake = deque([(0,0)]) # 머리, 몸통..,(꼬리)

while True:
    sec += 1
    head = snake[0] # 현재 머리 위치
    r, c = head[0] + move[dir_idx][0], head[1] + move[dir_idx][1]
    if sec in rotate:
        if rotate[sec] == 'D':
            # 순환하기 때문에 (% 4)로 나머지정리
            dir_idx = (dir_idx+1) % 4 # 현재 방향에서 오른쪽으로 회전했을 때 방향
        else:
            dir_idx = (dir_idx-1) % 4
    if not (0 <= r < n and 0 <= c < n) or (r, c) in snake:
        print(sec)
        break
    snake.appendleft((r, c)) # 새 머리 
    if board[r][c] == 1:
        board[r][c] = 0
    else:
        snake.pop()