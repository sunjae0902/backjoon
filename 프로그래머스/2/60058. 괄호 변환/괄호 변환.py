def is_correct(p): # 올바른
    st = []
    for c in p:
        if c == ')':
            if st and st[-1] == '(':
                st.pop()
        else:
            st.append(c)
    if st == [] and is_equal(p):
        return True
    return False
                
def is_equal(p): # 균형
    return p.count('(') == p.count(')')

def split(p):
    u, v = '', ''
    for i in range(len(p)):
        if is_equal(p[:i+1]):
            u = p[:i+1]
            v = p[i+1:]
            break
    return (u, v)

def reverse(p):
    p = list(p)
    for i in range(len(p)):
        p[i] = '(' if p[i] == ')' else ')'
    return ''.join(p)

def solution(p):
    if p == '':
        return ''
    if is_correct(p):
        return p
    u, v = split(p)
    
    if is_correct(u):
        return u + solution(v)
    else:
        res = '(' + solution(v)
        res += ')'
        res += reverse(u[1:len(u)-1])
        return res