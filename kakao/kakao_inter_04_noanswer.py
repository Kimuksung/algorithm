import copy
board = [[0,0,0],[0,0,0],[0,0,0]]

length = len(board)
board2 = [[0]*length]*length
board3 = copy.deepcopy(board)

devide = [0 , 1 , 2] #0 up #2 left #1 no


# initialize
for i in range( 0, length-1):
    if board[i+1][0] == 0:
        board2[i+1][0] = board2[i][0] + 100
        board3[i+1][0] =  devide[0]

for i in range( 0, length-1):
    if board[0][i+1] == 0:
        board2[0][i+1] = board2[0][i] + 100
        board3[0][i+1] = devide[1]

for i in range(1 , length):
    for j in range(1, length):
        print(i , j)
        if board3[i-1][j] == 2 and board3[i][j-1] ==2:
            board3[i][j] = 2
        else:
            up = 9999
            left = 9999
            if board3[i-1][j] != 2:
                
                if board3[i-1][j] == 1: #왼쪽에서 온경우
                    up = board2[i-1][j] + 600
                else : # 위쪽에서 온경우
                    up = board2[i-1][j] + 100
            if board3[i][j-1] != 2:                
                if board3[i][j-1] ==1: #왼쪽에서 온경우
                    left = board2[i][j-1] +100
                else: #위에서 온경우
                    left = board2[i][j-1] +600
            if up>=left: #left가 작은경우
                board2[i][j] = left
                board3[i][j] = devide[1]
            elif left>up: # up이 작은경우
                board2[i][j] = up
                board3[i][j] = devide[0]
            print("up" , up)
            print("left" , left)
        print(board2)
        
'''
        #위에서 내려온 경우
        up = board2[i-1][j] + board3[i-1][j]
        #왼쪽에서 내려온 경우
        left = board2[i][j-1] + board3[i][j-1]
        if( left > up  ): #위에서 온경우 같으면 왼쪽으로 처리
            board2[i][j] = up
            board3[i][j] = devide[0]
            
        else:
            board2[i][j] = left
            board3[i][j] = devide[1]
'''         
board2
board3
