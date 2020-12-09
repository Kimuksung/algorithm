import sys
sys.setrecursionlimit(10**6) #python은 재귀가 1000번까지만 돈다.

class Tree:
    def __init__(self , data , left = None , right = None):
        self.data = data
        self.left = left
        self.right = right
        
preorder_list = []
nextorder_list = []
def preorder( root , nodeinfos):
    preorder_list.append( nodeinfos.index(root.data) + 1)
    
    if root.left:
        preorder(root.left , nodeinfos)
    if root.right:
        preorder(root.right , nodeinfos)
    
    return preorder_list

def nextorder( root , nodeinfos):
    if root.left:
        nextorder(root.left , nodeinfos)
    if root.right:
        nextorder(root.right , nodeinfos)
    
    nextorder_list.append( nodeinfos.index(root.data) + 1)
    
    return nextorder_list

def solution(nodeinfos):
    
    root = None
    sorted_node = sorted( nodeinfos , key= lambda x : (x[1] , -x[0]) , reverse= True)
    print(sorted_node)
    for nodeinfo in sorted_node: # 모든 노드 돌면서 Tree 만들기
        if not root : # 초기 설정
            root = Tree(nodeinfo)
        else:  # Tree에 추가
            current = root # root부터 자기에 해당되는 값 찾아 들어간다.
            while True  :
                if current.data[0] > nodeinfo[0]:
                    if current.left  :#왼쪽 자식이 있는지 여부
                        current = current.left
                        continue
                    else:
                        current.left = Tree(nodeinfo)
                        break
                else:
                    if current.right  :#우측 자식이 있는지 여부
                        current = current.right
                        continue
                    else:
                        current.right = Tree(nodeinfo)
                        break
                
    preorder_answer = preorder( root , nodeinfos)
    nextorder_answer = nextorder(root , nodeinfos)
    answer =[]
    answer.append(preorder_answer)
    answer.append(nextorder_answer)
    return answer
        



nodeinfos = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
solution(nodeinfos)