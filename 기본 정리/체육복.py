def solution(n, lost, reserves):
    answer = 0
    
    for data in list(set(lost).intersection(set(reserves))):
        lost.remove(data)
        reserves.remove(data)
    
    for reserve in reserves:
        if reserve-1 in lost:
            lost.remove(reserve-1)
        elif reserve+1 in lost:
            lost.remove(reserve+1)
    
    answer = n - len(lost)
    
    return answer