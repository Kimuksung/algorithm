import math
def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    for i in range(n):
        progresses[i] = math.ceil ( ( 100 - progresses[i] ) / speeds[i] )
    
    print(progresses)
    max = progresses[0]
    count = 1
    
    for  i in progresses[1:]:
        if i > max:
            answer.append(count)
            count = 1
            max = i
        else:
            count += 1
            
    answer.append(count)
    return answer

progresses = [92]
speeds =  [3]
solution(progresses, speeds)