def solution(progresses, speeds):
    days = []
    n = len(progresses)

    for i in range(n):
        progresses[i] = [progresses[i], speeds[i]]
    
    st = progresses[::-1]

    while True:
        cnt = 0
        if sum(days) == n:
            break
        while st and st[-1][0] >= 100:
            st.pop()
            cnt += 1
        if cnt:
            days.append(cnt)
        for j in range(len(st)):
            st[j][0] += st[j][1]
    return days