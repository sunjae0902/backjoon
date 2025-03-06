def solution(name):
    answer = 0
    n = len(name)
    move = n - 1  # 좌우 이동 최소 횟수 (기본적으로 끝까지 가는 경우)
    for i, char in enumerate(name):
        # 위 아래 조작
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 연속된 'A'가 있는 경우 좌우 이동 최소값 갱신
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1
            
        # 끝까지 가는 경우 vs 현재 위치까지 갔다가 뒤로 돌아가는 경우 (왼쪽으로 턴 / )  비교
        move = min(move, i * 2 + (n - next_idx), (n - next_idx) * 2 + i)
    answer += move
    return answer