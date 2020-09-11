def solution(N, stages):
    answer = []
    
    stage_count = dict()
    answer_fail = dict()
    
    all_stage_clear = 0
    
    for stage in stages:
        if stage> N:
            all_stage_clear += 1
        else:
            if stage in stage_count.keys():
                stage_count[stage] += 1
            else:
                stage_count[stage] = 1           
            
    for i in range(1, N+1) :
        if i in stage_count.keys():
            current = stage_count[i]
            current2 = 0 
            for j in range(i+1,N+1):
                if j in stage_count.keys():
                    current2 += stage_count[j]                            
            answer_fail[i] = current / (current +current2 + all_stage_clear)
        else:
            answer_fail[i]= 0             

    
    answer = sorted(answer_fail , key =  answer_fail.get , reverse= True)
    return answer

N = 10
stages = [4,4,4,4,4,4,4,4,4,4]	
solution(N ,stages)
