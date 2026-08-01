from itertools import product

def solution(n, infection, edges, k):
    pipe = [[] for _ in range(4)]

    # 타입별 간선 저장
    for s, e, t in edges:
        pipe[t].append((s, e))
        pipe[t].append((e, s))

    answer = 1

    for length in range(1, k + 1):
        for order in product([1, 2, 3], repeat=length):

            infected = [False] * (n+1)
            infected[infection] = True

            # 파이프를 순서대로 개방
            for t in order:

                # 같은 파이프를 통해 더 이상 전파되지 않을 때까지 반복
                changed = True
                while changed:
                    changed = False

                    for s, e in pipe[t]:
                        if infected[s] and not infected[e]:
                            infected[e] = True
                            changed = True

            answer = max(answer, sum(infected))

    return answer