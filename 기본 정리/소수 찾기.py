from itertools import permutations
import math

def check( n ):
    sqrt_n = int( math.sqrt(n) + 1 )
    
    if n < 2:
        return False
    
    for i in range(2, sqrt_n):
        if n % i == 0:
            return False
    
    return True

def solution(numbers):
    answer = 0

    n = len(numbers)
    
    for i in range(1,n+1):
        datas = list( set( map(''.join , permutations( numbers , i)  ) ))
        for data in datas:
            if not data[0] == "0":                
                if check( int(data) ):
                    answer += 1
    
    return answer


numbers = "17"
solution(numbers)