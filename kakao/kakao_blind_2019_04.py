def check(food_times):
    for i in food_times:
        if i != 0:
            return False
    return True

def solution(food_times, k):
    answer = 0
    
    n = len(food_times)
    time = 0
    current = 0
    
    while(time<=k):
        #print(time)
        #print(food_times)
        if check(food_times):
            return -1
        while(food_times[current] == 0):
            
            current = (current+1) % n

        #print("current:",current+1)
        if food_times[current] > 0 :
            food_times[current] -= 1
            current = (current +1) % n
        time += 1
        
    answer = current
    if current ==0:
        answer = n
    
    return answer


food_times = [3,1,1,1,2,4,3]
k = 12
solution(food_times,k)

