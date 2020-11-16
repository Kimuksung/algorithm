def solution(priorities, location):
    answer = 0
    
    current = 0
    number = priorities[location]
    
    indexing = dict()
    for index , prioritie in enumerate(priorities):
        if prioritie in indexing.keys():
            indexing[prioritie].append(index)
        else:
            indexing[prioritie] = [index]

    for i in range(9,0,-1):
        if i == number:
            temp = indexing[i]
            left = []
            right = []

            for index , value in enumerate(temp):
                if value>= current:
                    right.append(value)
                else:
                    left.append(value)
            
            if location<current: #우측 다봐야함

                answer += len(right)
                for value2 in left:
                     if value2 <= location:
                        answer += 1   
            else:
                for value2 in right:
                    if value2 <= location:
                        answer += 1              
            break
        
        else:
            if i in indexing.keys():
                left = []
                right = []
                temp = indexing[i]

                for index , value in enumerate(temp):
                    if value> current:
                        right.append(value)
                        answer = answer+1
                    else:
                        left.append(value)
                        answer = answer+1
                if left:
                    current = max(left)
                else:
                    current = max(right)
    
    return answer
priorities = [1, 1, 9, 1, 1, 1]
location = 0
solution(priorities, location)
