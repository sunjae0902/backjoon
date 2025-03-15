from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights, bridge = deque(truck_weights), deque() # 다리에 있는 트럭 [진입시간, 무게]
    while True:
        if not truck_weights and not bridge:
            break
        answer += 1
        if bridge and bridge[0][0] + bridge_length == answer:
            bridge.popleft()
        if truck_weights and len(bridge) + 1 <= bridge_length and sum([m[1] for m in bridge]) + truck_weights[0] <= weight:
            now = truck_weights.popleft()
            bridge.append((answer, now))

           
    return answer