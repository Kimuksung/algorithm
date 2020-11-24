from collections import deque

def solution(prices):
    answer = []
    
    stack = deque() 
    prices = prices[::-1]
    for index , value in enumerate(prices[1:]):
        print(value)
        print(stack)
        if not stack : #stack에 추가 / 스택이 없거나 / 스택에서 뽑은값이 더 작으면
            stack.append([value, index+1])
        else:
            stack_value , stack_index = stack.pop()
            stack.append([stack_value , stack_index])
            
            if stack_value < value:
                stack.appendleft( [ value , 1] )
            
            else:
                count = 0
                print("here", sum( v>=2 for v, k in stack))
                
        
    return answer

prices = [1, 2, 3, 2, 3]	
solution(prices)

stack = deque()