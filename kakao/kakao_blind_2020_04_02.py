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

def solution(words, queries):
    answer = []
    
    word_trie = {}
    reverse_trie = {}
    
    for word in words:
        n = len(word)
        if not n in word_trie.keys():
            t = Trie()
            t.insert_string(word)
            word_trie[n] = t
    
            i = Trie()
            i.insert_string(word[::-1])
            reverse_trie[n] = i
            
        else:
            t = word_trie[n]
            t.insert_string(word)
            
            i = reverse_trie[n]
            i.insert_string(word[::-1])
            
    for query in queries:
        n = len(query)
        
        if not n in word_trie.keys():
            answer.append(0)
        else:
            if "?"*n == query:
                answer.append(word_trie[n].first_count())
            if not query[0] == "?":
                temp = query.split("?")[0]
                answer.append(word_trie[n].find(temp))
                
            elif not query[-1] == "?":
                temp = query.split("?")[-1]
                answer.append(reverse_trie[n].find(temp))
            else:
                word_trie[n].find(query)
    return answer


words =["abcde", "abc", "abcd", "abcdf"]
queries = ["?????" , "???" , "abc??" , "abc?" ,"abcde"]
solution(words, queries)
