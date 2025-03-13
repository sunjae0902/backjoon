from itertools import permutations
import math

def is_prime(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    numbers = list(numbers)
    for i in range(1, len(numbers)+1):
        for perm in permutations(numbers, i):
            num = int(''.join(perm))
            if num not in answer and is_prime(num):
                answer.add(num)
    return len(answer)