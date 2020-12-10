import collections

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    truck_weights = collections.deque(truck_weights)
    
    bridge = collections.deque([0 for i in range(bridge_length)])
    sum_bridge = 0
    while(truck_weights):
        sum_bridge -= bridge.popleft()
        if sum_bridge + truck_weights[0] <= weight:
            data = truck_weights.popleft()
            sum_bridge += data
            bridge.append(data)           
        else:
            bridge.append(0)
        answer+=1
    answer += bridge_length
    return answer


bridge_length = 100
weight = 100
truck_weights =	[10,10,10,10,10,10,10,10,10,10]
solution(bridge_length, weight, truck_weights)