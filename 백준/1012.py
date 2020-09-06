import sys
sys.setrecursionlimit(50000)
t = int(input())

def DFS( x ,  y ):
    all_map[y][x] = 0
    visited[y][x] = 1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<= nx <n and 0<= ny < m:
            if visited[ny][nx] !=1 and all_map[ny][nx] ==1:
                DFS(nx,ny)
    visited[y][x] = 0
    
for i in range(t):
    n , m , k = map( int , input().split())
    
    all_map = [[0 for i in range(n)] for _ in range(m)]
    #initialize
    for i in range(k):
        x,y = map(int ,input().split())
        all_map[y][x] =1
    
    visited = [[0 for i in range(n)] for _ in range(m)]
        
    dx , dy = [1,-1,0,0] , [0,0,-1,1]
    
    count = 0
    for i in range(n):
        for j in range(m):
            if all_map[j][i] == 1:
                DFS(i,j)
                count+=1
    
    print(count)
