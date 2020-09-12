from collections import deque

def BFS_find(graph , start , end , weight_list):
    visited = []
    weight = [9999 for _ in range(201) ]
 
    queue = deque([start])
    weight[start] = 0
    while queue:
        n = queue.popleft()
        
        if n not in visited:
            visited.append(n)

            if n in graph.keys():
                will_go = list(set(graph[n]) - set(visited))
                queue += will_go
                for i in will_go:
                    if weight[i] > weight_list[(n,i)] + weight[n]:
                        weight[i] = weight_list[(n,i)] + weight[n]
           
    return weight
     
def solution(n, s, a, b, fares):
    answer = []
    
    graph_list = {}
    weight_list = {}

    for x,y,value in fares:
        weight_list[(x,y)] = value
        weight_list[(y,x)] = value
        if x in graph_list.keys():
            graph_list[x].append(y)
            
        else:
            graph_list[x] = [y]
        if y in graph_list.keys():
            graph_list[y].append(x)
        else:
            graph_list[y] = [x]
    
    temp = []

    a_to_b = BFS_find(graph_list , a,b , weight_list)
    b_to_a = BFS_find(graph_list , b,a , weight_list)
    
    for ele1, ele2 in zip(a_to_b,b_to_a):
        temp.append(ele1+ele2)
    
    m = min(temp)
    print([i for i, j in enumerate(temp) if j == m])
    
    temp2 = []
    for index in [i for i, j in enumerate(temp) if j == m]:
        temp2.append(BFS_find(graph_list , s,m , weight_list))
    m = min(temp2)
    s_to_m = BFS_find(graph_list , s,m , weight_list)
    m_to_a = BFS_find(graph_list , m,a , weight_list)
    m_to_b = BFS_find(graph_list , m,b , weight_list)
    return s_to_m+m_to_a_+m_to_b


n , s, a, b  =7	,3	,4	,1
fares = 	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
solution(n, s, a, b, fares)