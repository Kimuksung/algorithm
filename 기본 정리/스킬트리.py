def solution(skill, skill_trees):
    answer = 0
    
    for skill_tree in skill_trees:
        skill_list = list(skill)   
        for i in skill_tree:
            if i in skill_list and skill_list.pop(0) != i:
                break
        else:
            answer += 1
    
    return answer

skills = "CBD"
skill_trees = ["BACDE", "CBADF", "AECB", "BDA"]
solution(skills , skill_trees)