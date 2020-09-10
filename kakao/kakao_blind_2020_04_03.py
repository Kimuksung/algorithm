class Node(object):
    def __init__( self , key , count = 0):
        self.key = key
        self.count = count       
        self.children = {}
        
class Trie(object):
    def __init__(self ):
        self.head = Node(key = None , count = 0)
    
    def insert_string(self , input_strings):
        current_node = self.head
        for input_string in input_strings:
            if not input_string in current_node.children.keys(): # 해당 root 아래에 존재 하지 않는 경우
                current_node.children[input_string] = Node(key = input_string , count = 1)
                current_node = current_node.children[input_string]
            else: # 해당 root 아래에 존재 하는 경우
                current_node = current_node.children[input_string]
                current_node.count += 1
                
    def find(self , input_strings):
        current_node = self.head
        cnt1 = 0
        for input_string in input_strings:
            if not input_string in current_node.children.keys():
                return 0
            current_node = current_node.children[input_string]
            cnt1 = current_node.count

        return cnt1
    
    def first_count(self):
        cnt = 0
        for i in self.head.children.keys():
            cnt += self.head.children[i].count

        return cnt
    
    
def solution( words  , queries):
    answer= []    
    front = {}
    back = {}
    
    for word in words:
        n = len(word)
        if n in front.keys():
            trie = front[n]
            reverse_trie = back[n]

            trie.insert_string(word)            
            reverse_trie.insert_string(word[::-1])


        else:
            temp = Trie()
            temp2 = Trie()
            #print(word[::-1])
            temp.insert_string(word)
            temp2.insert_string(word[::-1])
            front[n] = temp
            back[n] = temp2
            
     
    for query in queries:
        n = len(query)
        if n in front.keys():

            front_trie = front[n]
            back_trie = back[n]

            if query == "?"*n:     

                answer.append(front_trie.first_count())
            elif query[0]=="?":

                temp = query[::-1].split("?")[0]
                print(temp)
                answer.append(back_trie.find(temp))
            else:
                temp = query.split("?")[0]
                answer.append(front_trie.find(temp))
        else:
            answer.append(0)

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
solution( words  , queries)

