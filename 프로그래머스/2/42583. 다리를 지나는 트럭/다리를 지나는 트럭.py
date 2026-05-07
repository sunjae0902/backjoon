from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    # 대기중인 트럭과 다리에 있는 트럭을 큐로 관리
    truck_weights, bridge = deque(truck_weights), deque() # 다리에 있는 트럭 [진입시간, 무게]
    while True:
        if not truck_weights:
            break
        answer += 1
        # 현재 시간을 기준으로 완료 시각을 계산해서 비교
        if bridge and bridge[0][0] + bridge_length == answer:
            bridge.popleft()
        if len(bridge) < bridge_length and sum([m[1] for m in bridge]) + truck_weights[0] <= weight:
            now_w = truck_weights.popleft()
            bridge.append((answer, now_w))

    if bridge:
        answer += bridge_length
           
    return answer