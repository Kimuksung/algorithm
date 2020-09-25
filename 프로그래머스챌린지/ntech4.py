t1 = [[1,2],[3,4],[5,6],[-1,7],[8,9],[-1,-1],[-1,-1],[-1,-1],[-1,-1],[-1,-1]]
t2 = [[1,2],[-1,-1],[-1,-1]]

def check_tree(a,b):  
    if t1[a] is [-1,-1] and t2[b] is [-1,-1]:
        return True
    
    t1_x , t1_y = t1[a]
    t2_x , t2_y = t2[b]
    if t1_x != -1:
        t1_x = 1
    if t1_y != -1:
        t1_y = 1
    if t2_x != -1:
        t2_x = 1
    if t2_y != -1:
        t2_y = 1
    
    if t1[a] is not [-1,-1] and t2[b] is not [-1,-1]:
        return (t1_x == t2_x) and (t1_x == t2_x) and check_tree(t1[t1_x],t2[t2_x]) and check_tree(t1[t1_y] , t1[t2_y])

    return False

check_tree(2,0)

import collections
deq = collections.deque([0])

while(deq):
    current = deq.popleft()
    print("current:",current)

    i,j = t1[current]
    print(i,j)
    if i != -1:
        deq.append(i)
        print(j)
    if j != -1:
        deq.append(j)
    
    

