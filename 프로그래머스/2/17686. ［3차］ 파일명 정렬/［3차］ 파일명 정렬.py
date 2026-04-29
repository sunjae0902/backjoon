def parse(name):
    i = 0
    while i < len(name) and not name[i].isdigit():
        i += 1
    start = i # 숫자 시작 위치
    
    while i < len(name) and name[i].isdigit() and i - start < 5:
        i += 1
    
    h = name[:start]
    n = name[start:i]
    t = name[i:]
    
    return h, n, t
            
def solution(files):
    answer = []
    for i, name in enumerate(files):
        h, n, t = parse(name)
        answer.append((name, h, n, t, i))
    answer.sort(key = lambda x: (x[1].lower(), int(x[2]), x[4]))

    return [x[0] for x in answer]