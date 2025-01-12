import sys
from collections import defaultdict
input = sys.stdin.readline
# 구현, 케이스 분류 ..
while True:
    board = input().strip()
    if board == "end":
        break
    positions = defaultdict(list)
    for i in range(len(board)):
        positions[board[i]].append(i) # 인덱스를 리스트로 저장

    x_count, o_count, empty = (
        len(positions["X"]),
        len(positions["O"]),
        len(positions["."]),
    )
# O가 더 많거나, X와 O의 차이가 2개 이상 나는 경우
    if x_count < o_count or x_count > o_count + 1:
        print("invalid")
        continue

    winning_combinations = [
        {0, 1, 2},
        {3, 4, 5},
        {6, 7, 8},  
        {0, 3, 6},
        {1, 4, 7},
        {2, 5, 8},  
        {0, 4, 8},
        {2, 4, 6},  
    ]
    # x와 o에 각각 가로, 세로, 대각선 조합이 존재하는지
    x_wins = any(comb.issubset(positions["X"]) for comb in winning_combinations)
    o_wins = any(comb.issubset(positions["O"]) for comb in winning_combinations)
    
    # 둘 다 존재할 수 없음
    if x_wins and o_wins:
        print("invalid")
        continue

    # x, o의 개수가 같은데 x가 이길 수 없음
    if x_wins and x_count == o_count:
        print("invalid")
        continue

    # x와 o의 개수가 다른데 o가 이길 수 없음
    if o_wins and x_count != o_count:
        print("invalid")
        continue

    # 꽉 차있고 둘 다 존재하지 않으면 가능
    if empty == 0 and not (x_wins or o_wins):
        print("valid")
        continue

    # 빈 칸이 1개 이상인데 둘 다 존재하지 않는 경우 -> 아직 안끝난 상태
    if not x_wins and not o_wins and empty > 0:
        print("invalid")
    else:
        print("valid")