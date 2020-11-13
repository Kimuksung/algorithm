def solution(participants, completions):
    answer = ''
    
    dictionary = dict()
    
    for participant in participants:
        if not participant in dictionary.keys():
            dictionary[participant] = 1
        else:
            dictionary[participant] =  dictionary[participant] + 1
        
    for completion in completions :
        if completion in dictionary.keys():
            dictionary[completion] = dictionary[completion] - 1
    
    for k,v in dictionary.items():
        if v != 0:
            answer=k
    
    return answer