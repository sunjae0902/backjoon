from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    d, sales = defaultdict(int), defaultdict(int)
    
    for i in range(len(want)):
        d[want[i]] = number[i]

    for i in range(10):
        sales[discount[i]] += 1
        
    i = 0
    while i < len(discount) - 9: 
        if sales == d:
            answer += 1
        if i + 10 < len(discount):
            sales[discount[i]] -= 1
            if sales[discount[i]] == 0:
                sales.pop(discount[i])
            sales[discount[i+10]] += 1
        i += 1  
    return answer