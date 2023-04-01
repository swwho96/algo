from collections import deque
def solution(bridge_length, weight, truck_weights):
    time, insert, out = 0,0,0
    truck_weights = truck_weights[::-1]
    bridge = deque([0 for _ in range(bridge_length)])
    
    while len(truck_weights) != 0: # 트럭이 모두 다리위로 올라가면 종료
        time += 1
        next_truck = truck_weights[-1]
        now_bridge = insert - out # 다리 위 트럭 무게 = 올라간 트럭무게 - 나간 트럭 무게
        next_step = next_truck + now_bridge 
        if next_step <= weight or next_step - bridge[-1] <= weight:
            insert += truck_weights.pop()
            out += bridge.pop()
            bridge.appendleft(next_truck)
        else:
            out += bridge.pop()
            bridge.appendleft(0)
    return time + bridge_length

# ------------------------------------------------------------------

from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_weight = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    while truck_weights or bridge_weight != 0:
        time += 1
        tmp = 0
        if truck_weights and (bridge_weight+truck_weights[0]-bridge[0]) <= weight:
            tmp = truck_weights.popleft()
        bridge_weight -= bridge.popleft()
        bridge_weight += tmp
        bridge.append(tmp)
    return time