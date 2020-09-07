from collections import deque

def BFS(x,y,count , direct):
    visited = [[0 for i in range(n)] for _ in range(n)]
    
    dx , dy = [1,-1,0,0],[0,0,-1,1]
    
    queue = deque([(x,y,count,direct)])
    
    while(queue):
        x,y,count,direct = queue.popleft()
        
        if x == n-1 and y == n-1:
            answer.append(count)
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<= nx < n and 0<= ny <n:
                next_count = count
                next_direct = ""
                
                if abs(nx-x)>0:
                    next_direct = "x"
                    next_count+=100
                    if next_direct != direct:
                        next_count+=500
                if abs(ny-y)>0:
                    next_direct = "y"
                    next_count+=100
                    if next_direct != direct:
                        next_count+=500
                
                if new_board[ny][nx] ==0:
                    if visited[ny][nx]==0 or visited[ny][nx] > next_count:
                        visited[ny][nx] = next_count
                        queue.append((nx,ny,next_count, next_direct))

def solution(board):
    global answer, visited , n,new_board
    answer = []
    
    n = len(board)
    new_board =board.copy()
    BFS(0,0,0,"x")
    BFS(0,0,0,"y")
    return min(answer)

board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
solution(board)


