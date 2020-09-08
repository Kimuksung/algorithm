def split_str(string , length):
    choose_string = string[:length]
    answer= ""
    cnt = 0
    current = 0
    split_string = [string[i:i+length] for i in range(0, len(string), length)]
    for i in split_string:
        if i!=choose_string:
            break
        cnt += 1
        current += length
        
    if cnt != 1:
        answer += str(cnt)
    answer+=choose_string
    return answer , string[current:] 

def solution(s):
    answer = dict()
    
    n = len(s)
    if n== 1:
        return 1
    for i in range(1, n//2 + 1):
        data = s
        temp = ""
        while(data):
            word , data = split_str(data , i)
            temp += word
    
        answer[i] = len(temp)   
    answer =min(answer.values())
    return answer
        
print(solution("a"))
