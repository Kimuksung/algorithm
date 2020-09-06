import sys
sys.setrecursionlimit(50000)

n,m = 3,3
arr = [ [0 for i in range(n)] for _ in range(m)]

dx , dy = [ 1,-1,0 , 0 ] , [0,0,-1,1]

all_map = [[0 for i in range(n)] for _ in range(m)]

def DFS( x ,  y ,  l):
    global answer
    if x == n-1 and y== m-1:
        if answer> l:
            answer = l
    
    all_map[x][y] = 1
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        
        if 0<=nx < n and 0<= ny < m:
            if all_map[nx][ny] != 1:
                DFS(nx,ny,l+1)
    
    all_map[x][y] = 0

       
DFS(0,0,1)
answer 
