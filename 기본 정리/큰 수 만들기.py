def solution(numbers, k):
    answer = ''

    stack = []
    stack.append(numbers[0])
    
    for index , number in enumerate(numbers[1:]):     # stack / k / 선택된 숫자

        if k==0: # 종료 조건
            for data in stack:
                answer += data
            answer += numbers[index+1:]
            break
        
        if stack[-1] >= number : #새로 들어온 값이 작다.
            stack.append(number)
          
        else:
            while(stack): # 새로 들어온 값이 크다면 갱신이 필요 작은 값들은 삭제해야할 필요가 잇음
                if stack[-1] < number and k>0:
                    stack.pop()
                    k -= 1
                else:
                    break
            stack.append(number)       

    if len(answer) == 0: # 예외 처리 알맞게 끝난 경우
        for data in stack:
            answer += data

    if k!=0: # 예외 처리동일 숫자가 반복되어서 나올 경우
        stack = stack[:-k]
        answer = ''
        for data in stack:
            answer += data
            
    return answer

number ="7777"
solution(number, 2)
