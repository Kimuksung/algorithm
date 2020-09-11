def solution(n)    :
    
    arr = [[0 for i in range(n)] for _ in range(n)]
    visited = [[0 for i in range(n)] for j in range(n)]
    for y in range(n-1):
        for x in range(y+1,n):
            visited[y][x] = 1

    dx , dy = [0,1,-1] , [1,0,-1]

    cnt = 1
    x , y = 0 , 0
    arr[x][y] = 1
    while(True):
        no_go = 0
        for i in range(3):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<= nx < n and 0<=ny <n:
                if visited[ny][nx] == 0:
                    cnt +=1
                    arr[ny][nx] = cnt 
                    visited[ny][nx] = 1
                    x = nx
                    y = ny
                    break
                if visited[nx][ny] == 1:
                    no_go += 1
                    if no_go == 3:
                        return arr
                
solution(4)

visited = [[1 if i>j else 0 for i in range(n)] for j in range(n)]
