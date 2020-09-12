import itertools
class Node(object):
    def __init__( self , key , count = 0):
        self.key = key
        self.count = count
        self.children = {}

class Trie(object):
    def __init__(self ):
        self.head = Node(key = None , count = 0)

    def insert_string(self , insert_arr ):
        current_node = self.head
        
        for insert_data in insert_arr:
            if not insert_data in current_node.children.keys():
                current_node.children[insert_data] = Node(key = insert_data , count = 1)
                current_node = current_node.children[insert_data]
            
            else: # 해당 root 아래에 존재 하는 경우
                current_node = current_node.children[insert_data]
                current_node.count += 1    

    def find(self , find_arr ,num):
        current_node = self.head       
        for find_one in find_arr:
            if find_one in current_node.children.keys():
                current_node = current_node.children[find_one]
            else:
                return 0
        answer = 0
        
        for childrens in current_node.children.keys():
            if int(childrens) >= num:
                answer += current_node.children[childrens].count

        return answer

def solution(info, query):
    answer = []
    t = Trie()
    for info_data in info:
        t.insert_string(info_data.split())
        
    for query_data in query:
        count = 0
        find_arr = query_data.split(" and ")[:-1]
        pizza, num = query_data.split(" and ")[-1].split()
        find_arr.append(pizza)
        
        cnt = 0
        arr = []
        for data in find_arr :
            if data !="-":
                arr.append([data])
            elif data == "-":
                if cnt ==0:
                    arr.append(["java","python","cpp"])
                if cnt ==1:
                    arr.append(["backend","frontend"])
                if cnt ==2:
                    arr.append(["junior","senior"])
                if cnt ==3:
                    arr.append(["pizza","chicken"])
            cnt += 1
        
        for test in list(itertools.product(*arr)):
            #print(list(test))
            #print(t.find(list(test) , int(num)))
            count += t.find(list(test) , int(num))
        answer.append(count)
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
solution(info, query)

