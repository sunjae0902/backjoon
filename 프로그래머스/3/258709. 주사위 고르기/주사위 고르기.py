from itertools import combinations

def solution(dice):
    n = len(dice)
    max_win_rate = 0
    best_combination = []

    for a_dice_indices in combinations(range(n), n//2): # 주사위 조합 구하기
        b_dice_indices = [i for i in range(n) if i not in a_dice_indices]
        
        # 모든 조합의 합 구해서 반환
        a_sums = generate_sums([dice[i] for i in a_dice_indices])
        b_sums = generate_sums([dice[b] for b in b_dice_indices])
        
        # Count wins more efficiently
        wins = count_wins(a_sums, b_sums)
        
        # Update best combination if win rate is higher
        if wins > max_win_rate:
            max_win_rate = wins
            best_combination = list(a_dice_indices)

    return [x+1 for x in best_combination]

def generate_sums(selected_dice):
    from itertools import product # 두 개 이상 리스트의 모든 조합 반환
    return [sum(combination) for combination in product(*selected_dice)]

def count_wins(a_sums, b_sums):
    # 이진탐색을 위해 구한 합을 오름차순 정렬
    a_sums.sort()
    b_sums.sort()
    
    wins = 0
    for a_sum in a_sums:
        # a_sum으로 이긴 횟수 (B의 합들 중에 a_sum보다 작은 개수)
        wins += binary_search(b_sums, a_sum)
    return wins

def binary_search(arr, target):
    # A의 특정 합보다 작은 B의 합 개수를 구함.
    left, right = 0, len(arr)
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1 # 오른쪽으로 계속 탐색 
        else:
            right = mid # mid까지로 탐색 범위 좁힘
    return left