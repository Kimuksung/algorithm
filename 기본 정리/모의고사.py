def solution(answers):
    answer = []

    first = [1,2,3,4,5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5,3,3,1,1,2,2,4,4,5,5]
    
    n = len(answers)
    first_n = 5
    second_n = 8
    third_n = len(third)
    
    first_ans=0
    second_ans = 0
    third_ans = 0
    #한번의 싸이클을 돌때 몇개 맞는지 * 나누기 값 + 나머지값 순차
    for index,value in enumerate(answers):
        if first[index%5] == value:
            first_ans += 1
            
    for index,value in enumerate(answers):
        if second[index % 8] == value:
            second_ans += 1
            
    for index,value in enumerate(answers):
        if third[index%10] == value:
            third_ans += 1
        
    temp = dict()
    temp[1] = first_ans
    temp[2] = second_ans
    temp[3] = third_ans
    
    max_num = max(temp.values())
    for k,v in temp.items():
        if v == max_num:
            answer.append(k)
    
    answer = sorted(answer )
    return answer