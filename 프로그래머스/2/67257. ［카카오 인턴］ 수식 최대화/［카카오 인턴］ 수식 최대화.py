from itertools import permutations

def cal(a, b, op):
    if op == '+': return a+b
    if op == '-': return a-b
    if op == '*': return a*b

def solution(expression):
    answer = 0
    orders = []
    for perm in permutations(['+', '-', '*']):
        orders.append(perm)
        
    def parse(exp):
        num = ''
        result = []
        for c in exp:
            if c in ['+', '-', '*']:
                result.append(num)
                result.append(c)
                num = ''
            else:
                num += c
        result.append(num)
        return result
        
    exp = parse(expression)
    
    for f, s, t in orders:
        priority = {f: 0, s: 1, t: 2} # 우선순위, 클 수록 높음
        st = []
        op = []
        for term in exp:
            if term in priority:
                while op and priority[term] <= priority[op[-1]]:
                    a, b = st.pop(), st.pop()
                    st.append((cal(b, a, op.pop()))) # 계산 결과 저장
                op.append(term)
            else:
                st.append(int(term))
        while op:
            a, b = st.pop(), st.pop()
            st.append(cal(b, a, op.pop())) # 계산 결과 저장
        answer = max(answer, abs(st[0]))
    return answer
