def solution(numbers):
    
    def bin_arr(n):
        return list(map(int, bin(n)[2:])) #0b로 시작하는 문자열
    
    def make_full_tree(arr):
        n, size = len(arr), 1
        while size < n:
            size = 2*size + 1
        return [0] * (size-n) + arr
    
    def valid(l, r): # 배열 이진 탐색
        if l == r:
            return True
        
        mid = (l + r) // 2
        root = arr[mid]

        if root == 0: # 핵심 조건: 부모가 0인데 자식이 1일 수 없음
            if any(arr[l:r+1]):
                return False
            
        return valid(l, mid-1) and valid(mid+1, r)

            
    answer = []
    for n in numbers:
        arr = make_full_tree(bin_arr(n))
        answer.append(1 if valid(0, len(arr)-1) else 0)
        
    return answer