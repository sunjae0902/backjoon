from collections import defaultdict

def recur(now, amount, tree, amount_dict):
    if now == '-' or amount == 0:
        return
    mine, rem = (amount - amount // 10, amount // 10) if amount // 10 >= 1 else (amount, 0)
    amount_dict[now] += mine
    recur(tree[now], rem, tree, amount_dict)
            
def solution(enroll, referral, seller, amount):
    answer = []
    tree = defaultdict(str)
    amount_dict = defaultdict(int)
    
    for i in range(len(enroll)):
        tree[enroll[i]] = referral[i]
    
    for i in range(len(seller)):
        recur(seller[i], amount[i] * 100, tree, amount_dict)
        
    for name in enroll:
        answer.append(amount_dict[name])
    return answer