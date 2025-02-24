import sys
input = sys.stdin.readline

arr = input().rstrip()
answer = 0
stack = []

for i in range(len(arr)):
    if arr[i] == "(":
        stack.append("(")  
    else:  
        stack.pop()  
        if arr[i - 1] == "(":  # 레이저라면
            answer += len(stack)  # 현재 스택 크기(겹치는 막대기 개수)만큼 조각 증가
        else:  # 막대기의 끝이면
            answer += 1  # 막대기 끝부분 조각 추가
print(answer)