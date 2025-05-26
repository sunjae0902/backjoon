def solution(order):
    answer = 0
    n = len(order)
    cont, sub_cont = [i for i in range(n, 0, -1)], []

    for o in order:
        if cont and o == cont[-1]:
            cont.pop()
            answer += 1
            continue
        if sub_cont and o == sub_cont[-1]:
            sub_cont.pop()
            answer += 1
            continue
        while cont and o != cont[-1]:
            sub_cont.append(cont.pop())
        if cont and o == cont[-1]:
            cont.pop()
            answer += 1
        elif sub_cont and o == sub_cont[-1]:
            sub_cont.pop()
            answer += 1
        else: 
            break
    return answer