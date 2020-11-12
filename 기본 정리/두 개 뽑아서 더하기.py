# 프로그래머스 두 개 뽑아서 더하기

from itertools import permutations

def solution(numbers):
    temp = set()
    for k,v in list(permutations(numbers , 2)):
        #print(k)
        add_data = k+v
        temp.add(add_data)
    answer = list(temp)
    answer = sorted(answer)
    return answer

numbers =[5,0,2,7]
solution(numbers)