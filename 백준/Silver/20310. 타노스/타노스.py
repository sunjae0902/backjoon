import sys
input = sys.stdin.readline
arr = list(input().rstrip())

remove_one = arr.count("1") // 2
remove_zero = arr.count("0") // 2

s, e = 0, len(arr) - 1  
while remove_one > 0 or remove_zero > 0:
    if remove_one > 0 and arr[s] == "1":
        arr[s] = ""  # 제거 처리
        remove_one -= 1
    else:
        s += 1 
    if remove_zero > 0 and arr[e] == "0":
        arr[e] = ""  
        remove_zero -= 1
    else:
        e -= 1  
print("".join(arr))