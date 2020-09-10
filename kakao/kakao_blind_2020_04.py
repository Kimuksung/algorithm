def temp(items):
    cnt = 0
    u=""
    if items[0] =="?":
        for item in items:
            if item =="?":
                cnt += 1
            else:
                u+= item 
    else:
        for item in items:
            if item =="?":
                cnt +=1
            else:
                u += item
    return u , cnt , len(items)
    
def solution(words, queries):
    answer = []
    for query in queries:
        u , cnt , query_num = temp(query)
        count = 0
        for word in words:
            word_num = len(word)
            if query_num == word_num and word.startswith(u):
                count+=1
            elif query_num == word_num and word.endswith(u):
                count+=1
        answer.append(count)
    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao" , "tomto"]
queries = ["?????" , "?" ,"hello", "sex" , "to???"]
solution(words , queries)

