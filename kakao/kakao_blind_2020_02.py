def balance(string):
    cnt = 0
    current = 0
    for i in string:
        if i=="(":
            cnt +=1
            current += 1
        else: 
            cnt -=1
            current += 1
            
        if cnt == 0:
            break
        
    return string[:current] , string[ current:]

def right(string):
    cnt = 0

    for i in string:
        if i=="(":
            cnt += 1
        else:
            cnt -=1
        
        if cnt <0:
            return False
    return True
    
def change(string):
    answer =""
    for i in string:
        if i =="(":
            answer+= ")"
        else:
            answer += "("
    return answer

def solution(p):
    answer = ''
    if not p:
        return p
    
    u , v = balance(p)
    if right(u):
        u += solution(v)
        return u
    else:
        temp = "("
        temp += solution(v)
        temp += ")"
        
        temp += change( u[1:-1])
        
        return temp
    return answer

print(solution("()))((()"))
