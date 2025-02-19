def solution(n, w, num):
    answer = 0
    row = (num - 1) // w  
    col = (num - 1) % w  
    
    # 홀수 행일 경우 열 위치 반전
    if row % 2 == 1:
        col = w - 1 - col
    
    total_rows = (n - 1) // w  # 전체 행 수 
    for r in range(row, total_rows + 1):
        if r == total_rows:  # 마지막 행
            last_row_boxes = n % w
            if last_row_boxes == 0:
                last_row_boxes = w
            if r % 2 == 0:  # 왼쪽에서 오른쪽
                if col < last_row_boxes:
                    answer += 1
            else:  # 오른쪽에서 왼쪽
                if w - 1 - col < last_row_boxes:
                    answer += 1
        else:  # 마지막 행이 아닌 경우
            answer += 1   
    return answer