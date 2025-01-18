def solution(wallpaper):
    answer = [] # s~e 까지 선택, 거리: x변화량 + y 변화량, 최소인 시작, 끝 반환
     # x의 최소값, y의 최소값 중 더 작은 점부터, 최대중 가장 큰 값
    max_pos, min_pos = (0,0), (50, 50)
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == '#':
                if i+1 > max_pos[0] or j+1 > max_pos[1]:
                    max_pos = (max(i+1, max_pos[0]), max(j+1, max_pos[1]))
                if i < min_pos[0] or j < min_pos[1]:
                    min_pos = (min(i, min_pos[0]), min(j, min_pos[1]))
    answer.extend(list(min_pos) + list(max_pos))
      
    return answer