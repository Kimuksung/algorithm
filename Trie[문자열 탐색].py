class Node(object):
    def __init__(self, key, data=None):
        self.key=key # character 
        self.data=data # 기존 방식에서는 True/False로 집어넣지만, 여기서는 string or None을 집어넣음.
        self.children = {} # 해당 char에서 다른 캐릭터로 이어지는 children character(key)들과 각 Node(value)

class Trie(object):
    def __init__(self):
        self.head = Node(key=None, data=None)
    def insert_string(self, input_string):
        # Trie에 input_string을 넣어줌
        cur_node = self.head
        for c in input_string:
            if c not in cur_node.children.keys():
                cur_node.children[c] = Node(key=c)
            cur_node = cur_node.children[c]
        cur_node.data=input_string
    def search(self, input_string):
        # input_string이 현재 trie에 있는지 찾아서 TF를 리턴 
        cur_node = self.head
        for c in input_string:
            if c not in cur_node.children.keys():
                return False
            else:
                cur_node = cur_node.children[c]
        if cur_node.data==input_string:
            return True
        else:
            return False
    def start_with(self, prefix):
        # prefix로 시작하는 모든 워드를 찾아서 리턴합니다. 
        cur_node = self.head
        words = []
        subtrie = None
        for c in prefix:
            if c in cur_node.children.keys():# 있으므로 값을 하나씩 찾으며 내려감. 
                cur_node = cur_node.children[c]
                subtrie = cur_node
            else:# prefix가 현재 trie에 없으므로, 빈 리스트를 리턴 
                return []
        # 이제 prefix가 존재한다는 것을 알았고, subtrie에 있는 모든 워드를 찾아서 리턴하면 됨. 
        cur_nodes = [subtrie]
        next_nodes = []
        while True:
            for c in cur_nodes:
                if c.data!=None:
                    words+=[c.data]
                next_nodes+=list(c.children.values())
            #print("nn", [n.data for n in next_nodes])
            if len(next_nodes)==0:
                break
            else:
                cur_nodes = next_nodes
                next_nodes = []
        return words
##########################################
t = Trie()
t.insert_string("abcd")
t.insert_string("abdc")
t.insert_string("acbd")
t.insert_string("abkd")
t.insert_string("abzzzz")
t.search('abdc')
t.start_with('ab')