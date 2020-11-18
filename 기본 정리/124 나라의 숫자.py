temp_list = [ "4" , "0" , "1", "0", "2"] # change 

def third_base(n): #3진법 표현
    remainder = n % 3
    answer =""
    answer = str(remainder)+answer
    share = n//3
    while(share != 0):
        remainder = share % 3
        share = share//3        
        answer = str(remainder)+answer
    return answer

def change_str( temp ): # 4-> 2-> 1 변경
    if temp[0] == "0":
        return change_str(temp[1:])
    temp_str = ""
    for index , value in enumerate(temp):
        if value == "0":
            temp_str = temp_str[:-1] + temp_list[ int(temp[index-1])] + temp_list[int(temp[index]) ] + temp[index+1:]
            return change_str(temp_str)
        else:
            temp_str = temp_str + value
        
    temp = temp_str
    return temp
    
def solution(n):
    answer = ''
    
    #change 3진법
    change_thing = third_base(n)
    answer = change_str(change_thing)
    
    return answer

n= 500000000
#change_str('200')
solution(n)