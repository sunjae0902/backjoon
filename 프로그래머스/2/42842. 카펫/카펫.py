def solution(brown, yellow):
    answer = []
    extent = brown+yellow
    for width in range(3, yellow+3):
        height = extent // width
        if extent % width == 0 and height <= width:
            if height-2 == yellow // (width-2):
                answer.extend([width, height])
                break
    return answer
   