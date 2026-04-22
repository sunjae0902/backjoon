def convert(exp, n):
    exp_cp = exp[:]
    op1, op2, result = int(exp_cp[0], n), int(exp_cp[2], n), 0
    result = op1 + op2 if exp_cp[1] == '+' else op1 - op2
    tmp = []
    if result == 0:
        tmp.append('0')
    while result > 0:
        tmp.append(str(result % n))
        result //= n
    exp_cp[4] = ''.join(tmp[::-1])
    return ' '.join(exp_cp)

def valid(exp, n):
    return convert(exp, n).split()[-1] == exp[-1]
    
def solution(expressions):
    answer = []
    min_digit = 0
    mystery = []
    solved = []
    
    for exp in expressions:
        exp = exp.split()
        if 'X' in exp:
            mystery.append(exp)
        else:
            solved.append(exp)
        for st in exp:
            if st not in ['+', '-', '=', 'X']:
                for n in st:
                    min_digit = max(min_digit, int(n)+1)
    possible = set([i for i in range(min_digit, 10)])

    if len(possible) == 1:
        for exp in mystery:
            answer.append(convert(exp, list(possible)[0]))
    else:
        for n in list(possible):
            for exp in solved:
                if not valid(exp, n):
                    possible.remove(n)
                    break
        for exp in mystery:
            s = set()
            for n in possible:
                res_arr = convert(exp, n).split()
                s.add(res_arr[-1])
            if len(s) > 1:
                res_arr[-1] = '?'
            answer.append(' '.join(res_arr))
                    
    return answer