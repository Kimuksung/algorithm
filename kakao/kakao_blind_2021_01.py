import re

def solution(new_id):
    answer = ''
    
    first = new_id.lower()
    second = re.compile('[^ a-z0-9-._]')  
    second = second.sub('',first)

    third = re.compile('[.]+')
    third = third.sub('.',second)
    forth = third

    if third[0] ==".":
        forth = forth[1:]
    if third[-1]==".":
        forth = forth[:-1]
    
    five = forth
    if five == "":
        five = "a"
        
    six = five
    if len(six)>=16:
        six = six[:15]
        
    if six[-1]==".":
        six = six[:-1]
        
    answer =six

    while(len(answer)<=2):
        answer+=six[-1]
    
    return answer
solution("=.=")

