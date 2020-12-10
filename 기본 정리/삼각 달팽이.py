def solution(n):
    answer = []
    
    arr = [[0 for _ in range(n)] for _ in range(n) ]

    count = 0
    x,y = -1,0
    data = 1
    
    for i in range(n):
        for j in range(i,n):
            if count == 0 :
                x += 1 
            
            elif count == 1:
                y += 1
            else :
                x -= 1
                y-= 1

            arr[x][y] = data
            data += 1
        count = (count+1) % 3
    
    for row in arr:
        for row_data in row:
            if row_data:
                answer.append(row_data)
    
    return answer


n = 4
solution(n)
