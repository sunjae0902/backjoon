def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    days = []
    for i in range(n):
        days.append((100-progresses[i]-1) // speeds[i] + 1)
    s = [days[0]]
    for i in range(1, n):
        if days[i] <= max(s):
            s.append(days[i])
        else:
            answer.append(len(s))
            s = [days[i]]
    if s:
        answer.append(len(s))
    return answer