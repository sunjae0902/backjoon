def count_answer(arr, answers):
    cnt = 0
    for i in range(len(answers)):
        if answers[i] == arr[i]:
            cnt += 1
    return cnt

def get_arr(arr, answers):
    q, r = len(answers) // len(arr), len(answers) % len(arr)
    return arr * q + arr[:r]

def solution(answers): 
    answer = []
    people = [get_arr(arr, answers) for arr in [[1,2,3,4,5], [2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]]
    people = sorted([(count_answer(arr, answers),i+1 ) for i, arr in enumerate(people)], reverse = True, key = lambda x: x[0])
    answer.append(people[0][1])
    for i in range(1, len(people)):
        if people[i][0] == people[0][0]:
            answer.append(people[i][1])
        else:
            break
        
    return answer