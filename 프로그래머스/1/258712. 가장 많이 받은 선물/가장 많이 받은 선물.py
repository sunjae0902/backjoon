from collections import defaultdict

def solution(friends, gifts):
    answer = 0
    present_indices = defaultdict(int)
    history = defaultdict(list)
    count = defaultdict(int)
    
    for i in range(len(gifts)):
        a, b = map(str, gifts[i].split())
        present_indices[a] += 1
        present_indices[b] -= 1
        history[a].append(b)

    for i in range(len(friends)):
        for j in range(len(friends)):
            if i == j: continue
            a, b = friends[i], friends[j] 
            atob, btoa = history[a].count(b), history[b].count(a)
            if atob == btoa or (a not in history[b] and b not in history[a]):
                if present_indices[a] > present_indices[b]:
                    count[a] += 1
                elif present_indices[a] < present_indices[b]:
                    count[b] += 1
                else: continue
            else:
                if atob > btoa:
                    count[a] += 1
                elif atob < btoa:
                    count[b] += 1
    for c in count.values():
        answer = max(answer, c)
    return answer//2