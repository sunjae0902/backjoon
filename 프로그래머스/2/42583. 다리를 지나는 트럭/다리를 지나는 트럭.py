from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque()  # (트럭 무게, 다리에 진입한 시간) 저장
    total_weight = 0  # 현재 다리 위 트럭들의 총 무게
    truck_weights = deque(truck_weights)  # 대기 트럭 큐

    while truck_weights or bridge:
        answer += 1  # 시간 흐름
        
        # 다리를 지난 트럭 제거
        if bridge and bridge[0][1] + bridge_length == answer:
            total_weight -= bridge.popleft()[0]

        # 다리에 새로운 트럭 추가 가능 여부 확인
        if truck_weights and total_weight + truck_weights[0] <= weight and len(bridge) < bridge_length:
            truck = truck_weights.popleft()
            bridge.append((truck, answer))  # 트럭과 진입 시간을 저장
            total_weight += truck
    
    return answer
