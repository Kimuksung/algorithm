from itertools import combinations
def solution(relation):
    answer = 0
    n = len(relation)
    
    temp = dict()
    answer_list = list()
    for relation_word in relation:
        cnt = 0
        for relations in relation_word:
            if cnt in temp.keys():
                temp[cnt].append(relations)
            else:
                temp[cnt] = [relations]
            cnt +=1
    a = list(temp.keys())
    for i in range(n):
        for t in list(combinations(a,i)):
            print("--")
            temp2 = dict()
            for word in t:
                cnt = 0
                for ggg in temp[word]:
                    if cnt in temp2.keys():
                        temp2[cnt] += ggg
                    else:
                        temp2[cnt] = ggg
                    cnt +=1
            if len(set(temp2.values())) ==n:
                answer_list.append(t) 
    print(answer_list)
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
solution(relation)

