def solution(name):
    answer = 0
    name = name.lower()
    
    for char in name:
        number = ord(char) - 96
        if number <15:
            answer += number -1 
        else:
            answer += 26 - number +  1  
    print(answer)
    num = len(name)
    left , right = 0,0
    count = 0
    while True:
        
        if left < 0 :
            left = num-1
            
        if right > num-1 :
            right = 0
        
        if name[left] !="a":
            print(left, right)
            answer += count
        
        elif name[right] != "a":
            print(left, right)
            answer += count
        
        left -= 1
        right += 1
        count += 1
    return answer

name = "JEROEN"
solution(name)