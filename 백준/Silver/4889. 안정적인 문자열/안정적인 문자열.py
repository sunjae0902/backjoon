import sys
input = sys.stdin.readline
# 그리디
i = 1
while True:
    s = input().rstrip()
    if s[0] == '-' and len(s) >= 1:
        break
    stack = []
    count = 0
    for p in s:
        if p == '{':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                count += 1 # 짝이 안맞으니까 바꿈
                stack.append('{') # 바꾼 문자열 푸시
    # 항상 짝수 개만 남는다. 남은 수의 절반만큼 바꿔주면됨.
    print('%d. %d' %(i, count + len(stack) // 2))
    i += 1