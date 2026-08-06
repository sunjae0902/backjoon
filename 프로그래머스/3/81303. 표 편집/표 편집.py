def solution(n, k, cmd):
    answer = ['O'] * n
    prev = [i-1 for i in range(n)]
    next = [i+1 for i in range(n)]
    next[-1] = -1
    deleted = []
    
    for args in cmd:
        if len(args) == 1:
            if args == 'C':
                answer[k] = 'X'
                deleted.append((k, prev[k], next[k]))
                if prev[k] != -1:
                    next[prev[k]] = next[k]
                if next[k] != -1:
                    prev[next[k]] = prev[k]
                    
                if next[k] != -1:
                    k = next[k]
                else:
                    k = prev[k]
            else:
                rec, rec_p, rec_n = deleted.pop()
                answer[rec] = 'O'
                prev[rec] = rec_p
                next[rec] = rec_n
                if rec_p != -1:
                    next[rec_p] = rec
                if rec_n != -1:
                    prev[rec_n] = rec
        else:
            c, x = args.split(' ')
            x = int(x)
            if c == 'U':
                for _ in range(x):
                    k = prev[k]
            else:
                for _ in range(x):
                    k = next[k]
    
    return ''.join(answer)