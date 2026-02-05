from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)               # 대기 트럭
    bridge = deque([0] * bridge_length)         # 다리(칸 수 = bridge_length)
    cur_weight = 0                               # 현재 다리 위 총 무게
    time = 0

    while trucks or cur_weight > 0:
        time += 1

        # 1) 1초 경과: 맨 앞 칸이 다리에서 내려가면서 무게 감소
        left = bridge.popleft()
        cur_weight -= left

        # 2) 다음 트럭을 올릴 수 있으면 올리고, 아니면 0(빈칸) 넣기
        if trucks and cur_weight + trucks[0] <= weight:
            t = trucks.popleft()
            bridge.append(t)
            cur_weight += t
        else:
            bridge.append(0)

    return time
