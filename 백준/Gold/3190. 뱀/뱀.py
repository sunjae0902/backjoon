import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
snake = deque([(0, 0)])
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_idx = 0
for _ in range(k):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1 # 사과

rotate = {} # 회전 방향
l = int(input())
for _ in range(l):
    s, d = map(str, input().split())
    rotate[int(s)] = d

answer = 0
while True:
    answer += 1
    head = snake[0]
    nx = head[0] + move[dir_idx][0]
    ny = head[1] + move[dir_idx][1]
    if answer in rotate:
        dir_idx = (dir_idx + 1) % 4 if rotate[answer] == "D" else (dir_idx - 1) % 4
    if not (0 <= nx < n and 0 <= ny < n) or (nx, ny) in snake:
        break
    snake.appendleft((nx, ny))
    if board[nx][ny] == 1:
        board[nx][ny] = 0
    else:
        snake.pop()
print(answer)
