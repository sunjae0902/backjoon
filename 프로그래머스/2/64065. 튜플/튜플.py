def parse(string):
    res = []
    for sub in [string.split('},')]:
        for i in sub:
            s, e = 0, len(i)-1
            while i[s] == '{':
                s += 1
            while i[e] == '}':
                e -= 1
            res.append([int(x) for x in i[s:e+1].split(',')])
    return res

def solution(s):
    answer = []
    num_set = set()
    num = parse(s)
    num.sort(key = lambda x: len(x))
    for tp in num:
        for i in tp:
            if i not in num_set:
                num_set.add(i)
                answer.append(i)         
            
    return answer