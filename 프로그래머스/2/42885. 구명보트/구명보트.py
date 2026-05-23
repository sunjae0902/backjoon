def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    st = []
    for w in people:
        if st and st[-1] + w <= limit:
            st.pop()
            answer += 1
            continue
        st.append(w)
    answer += len(st)

    return answer