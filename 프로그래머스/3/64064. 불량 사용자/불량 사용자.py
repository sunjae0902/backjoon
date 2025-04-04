import math
from itertools import permutations 

def solution(user_id, banned_id):
    valid = set()
    banned_sets = [] # 각 문자열에 가능한 유저들 저장
    
    for banned in banned_id:
        tmp = []
        ind = [i for i in range(len(banned)) if banned[i] == '*']
        s1 = ''.join([b for b in banned if b != '*'])
        for user in user_id:
            s2 = ''.join([user[i] for i in range(len(user)) if i not in ind])
            if len(banned) == len(user) and s1 == s2:
                tmp.append(user)
        banned_sets.append(tmp)
        
    for perm in permutations(user_id, len(banned_id)): # 전체 경우의 수 구하기 
        if all(perm[i] in banned_sets[i] for i in range(len(banned_sets))):
            valid.add(tuple(sorted(perm))) # 정렬해서 중복 무시
  
    return len(valid)