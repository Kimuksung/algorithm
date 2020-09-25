import collections

def BFS(start , graph_list , n):
    num = 0
    deque = collections.deque([[start , num]])
    visited = [-1 for _ in range(n+1)]
    
    while(deque):
        
        v , count = deque.popleft()
        if visited[v] == -1:           
            visited[v] = count
            count += 1
            for i in graph_list[v]:
                deque.append([i,count])
    return visited    
    
def solution(n , edges):
    answer = 0
    graph_list = [ [] for _ in range(n+1)]
    
    for edge in edges:
        x,y = edge
        graph_list[x].append(y)
        graph_list[y].append(x)
    
    visited = BFS(1 , graph_list , n)
    visited_max = max(visited)
    answer = visited.count(visited_max)
    
    return answer


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

solution(n,edge)