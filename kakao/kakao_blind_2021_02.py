from itertools import combinations

def alphabet(s):
    return ''.join(sorted(s))

def solution(orders, course):
    answer = []
    for j in course:
        order_dict = dict()
        for order in orders:
            for i in list( combinations( order , int(j) )):
                temp =""
                for t in i:
                    temp += t
                temp = alphabet(temp)   
                if temp in order_dict.keys():
                    order_dict[temp] += 1
                else:
                    order_dict[temp] = 1
        if order_dict.values() and max(order_dict.values())>1:
            for i in [k for k,v in order_dict.items() if v == max(order_dict.values())]:
                answer.append(i)      
    return sorted(answer)
    
    

orders= ["XYZ", "XWY", "WXA"]
course = [2,3,4]
solution(orders,course)
