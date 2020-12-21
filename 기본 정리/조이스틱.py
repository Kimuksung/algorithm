def solution(names):
    answer = 0
    number = [min( ord(name) - ord('A'), (ord('Z') - ord(name) +1 )) for name in names ]
    
    index = 0
    
    while(True):
        answer += number[index]
        number[index] = 0
        
        if sum(number) == 0:
            break
        left , right = 1 , 1
        #index에서 왼쪽값 / 우측값 가까운거 구해본다.
        while(number[index - left] ==0):
            left += 1
        while(number[index + right] ==0):
            right += 1
        
        answer += left if left < right else right
        index += -1 * left if left < right else right
    
    return answer

names = "JAN"
solution(names)
