import sys
input = sys.stdin.readline
R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
stack = [[(0, 0), set(arr[0][0])]]
move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
answer = 0
while stack:
    now, visited = stack.pop()
    answer = max(answer, len(visited))
    for dx, dy in move:
        nx, ny = now[0]+dx, now[1]+dy
        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] not in visited:
            stack.append([(nx, ny), visited | {arr[nx][ny]}])
print(answer)
