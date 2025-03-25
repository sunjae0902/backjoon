def get_10_from_26(s):
    n = 0
    for char in s:
        n = n * 26 + (ord(char) - ord('a')) + 1
    return n

def get_26_from_10(n):
    result = []
    while n > 0:
        n -= 1
        result.append(chr(ord('a') + (n % 26)))
        n //= 26
    return ''.join(result[::-1])

def solution(n, bans):
    bans_to_ten = []
    for b in bans:
        bans_to_ten.append(get_10_from_26(b))
    bans_to_ten.sort()
    for b in bans_to_ten:
        if b <= n:
            n += 1 # 갱신
        else:
            break 
    return get_26_from_10(n)