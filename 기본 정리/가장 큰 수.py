def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = sorted(numbers  ,key = lambda x:x*3 , reverse = True)
    print(numbers)
    return str(int(''.join(numbers)))
    
numbers = [6 , 61 , 67 , 10, 2]
solution(numbers)
