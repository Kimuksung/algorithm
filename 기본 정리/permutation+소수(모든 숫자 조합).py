from itertools import permutations
import math

def check_not_zero(number):
    if number[0] == "0":
        return True
    else:
        False
        
def check_decimal(number):
    
    if check_not_zero(number) or number == "1":
        return False
    
    number = int(number)
    sqrt_num = int(math.sqrt(number))
    
    for i in range(2,sqrt_num+1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    answer = []
    numbers= list(map(str,numbers))
    n = len(numbers)
    
    for i in range(1,n+1):
        for natural_num in list(map(''.join , permutations(list(numbers) , i))):
            if check_decimal(natural_num):
                answer.append(natural_num)
    
    return answer

s="011"
solution(s)

