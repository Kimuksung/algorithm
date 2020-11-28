def solution(votes):
    if len(votes) == 1:
        return 0
        
    me = votes[0]
    everyone = votes[1:]
    
    count = 0 
    
    while(me <= max(everyone)):
        max_index = everyone.index(max(everyone))
        everyone[max_index] -= 1
        me += 1
        count += 1
    
    return count

votes = [1]
solution(votes)