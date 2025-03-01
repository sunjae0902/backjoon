import sys
input = sys.stdin.readline
while True:
    st = input().rstrip()
    if st == '.':
        break
    stack = []
    flag = 1
    for s in st:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    flag = 0
                    break
            else:
                flag = 0
                break
        elif s == ']':
            if stack:
                if stack[-1] == '[':
                    stack.pop()
                else:
                    flag = 0
                    break
            else:
                flag = 0
                break
    if not flag or stack != []:
        print('no')
    else:
        print('yes')