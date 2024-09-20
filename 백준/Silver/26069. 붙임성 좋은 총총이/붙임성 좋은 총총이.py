import sys
#sys.stdin = open('input.txt', 'r')  # 제출 시에는 이 줄을 제거하거나 주석 처리하세요.
input = sys.stdin.readline

N = int(input())  # 만난 기록의 수
connections = []  # 사람들의 만남 기록
dancing = ['ChongChong']  # 무지개 댄스를 추는 사람들 리스트

# 입력 받기
for _ in range(N):
    A, B = input().split()
    connections.append((A, B))

# 연결된 사람들 중 무지개 댄스를 추는 사람과 연결된 모든 사람을 찾아서 추가
for A, B in connections:
    if A in dancing and B not in dancing:
        dancing.append(B)
    elif B in dancing and A not in dancing:
        dancing.append(A)

# 무지개 댄스를 추는 사람 수 출력
print(len(dancing))
