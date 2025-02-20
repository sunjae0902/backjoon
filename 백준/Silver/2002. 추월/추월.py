import sys
input = sys.stdin.readline
N = int(input())
entrance = [input().strip() for _ in range(N)]
exit_order = {input().rstrip() : i for i in range(N)}

count = 0
max_exit_index = -1  # 현재까지 가장 마지막에 나간 차량의 순서

for car in entrance:
    if exit_order[car] < max_exit_index: # 현재 차량이 먼저 나감
        count += 1  # 추월한 차량 카운트 증가
    else:
        max_exit_index = exit_order[car]  # 가장 늦게 나간 차량 업데이트
print(count)