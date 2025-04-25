import math

def square_dist(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

def solution(m, n, startX, startY, balls):
    answer = []
    for ballX, ballY in balls:
        min_dist = float('inf')
        # 각 벽에 대해 반사된 공의 좌표 - A의 직선거리
        mirrors = [
            (-ballX, ballY),            # 좌측 벽
            (2*m - ballX, ballY),       # 우측 벽
            (ballX, -ballY),            # 하단 벽
            (ballX, 2*n - ballY)        # 상단 벽
        ]
        
        for mirrorX, mirrorY in mirrors:
            # 출발점과 목적점이 같은 선상에 있고 공을 관통하는 경우 제외
            if startX == ballX == mirrorX and (
                (startY < ballY < mirrorY) or (mirrorY < ballY < startY)):
                continue
            if startY == ballY == mirrorY and (
                (startX < ballX < mirrorX) or (mirrorX < ballX < startX)):
                continue
            dist = square_dist(startX, startY, mirrorX, mirrorY)
            min_dist = min(min_dist, dist)
        
        answer.append(min_dist)
    return answer
