def to_10(s):
    res = 0
    for i in s:
        res = res * 26 + ord(i) - ord('a') + 1
    return res

def to_26(n):
    res = ''
    while n > 0:
        n -= 1
        res += chr(97 + n % 26)
        n //= 26
    return res[::-1]

def solution(n, bans):
    remove = sorted([to_10(b) for b in bans])
    cnt = 0
    for b in remove:
        if b <= n:
            n += 1
        else:
            break
    return to_26(n)