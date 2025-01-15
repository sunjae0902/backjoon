import sys
input = sys.stdin.readline
T = int(input())

def calculate(expr):
    i = 0
    # 공백 먼저 처리: 숫자 병합
    while i < len(expr):
        if expr[i] == " ": 
            combined_number = expr[i - 1] * 10 + expr[i + 1]
            expr[i - 1] = combined_number  # 병합된 숫자를 이전 위치에 저장
            del expr[i : i + 2]  # 공백과 다음 숫자를 제거
            i -= 1  # 인덱스를 한 칸 뒤로 이동하여 리스트 축소 반영
        else:
            i += 1
    # 계산
    result = expr[0]
    i = 1
    while i < len(expr):
        oper = expr[i]
        if oper == "+":
            result += expr[i + 1]
        elif oper == "-":
            result -= expr[i + 1]
        i += 2
    return result

def dfs(d, cur_arr):
    res = []
    if d == N:
        cal = calculate(cur_arr.copy())
        if cal == 0:
            res.append(cur_arr[:])
        return res
    operation = ['+', '-', ' ']
    for o in operation:
        new_arr = cur_arr.copy()
        new_arr[2*d-1] = o
        res.extend(dfs(d+1, new_arr))
    return res

for i in range(T):
    N = int(input())
    arr = [0] * (2*N-1)
    for i in range(N):
        arr[2*i] = i+1
    res = dfs(1, arr)
    res.sort()
    for ans in res:
        for j in ans:
            print(j, end = '')
        print()
    print()