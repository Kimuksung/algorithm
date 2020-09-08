def moving(key , direct):
    n = len(key)
    arr = [[0 for i in range(n)] for _ in range(n)]
    
    
    if direct=="u":
        for i in range(n-1): #up
            arr[i] = key[i+1]
    if direct =="d":    
        for i in range(1,n): #down
            arr[i] = key[i-1]
    if direct =="l":
        for i in range(n):
            for j in range(n-1):
                arr[i][j] = key[i][j+1]
    if direct =="r":
        for i in range(n):
            for j in range(1,n):
                arr[i][j] = key[i][j-1]            
    return arr

def rotate_90(key):
    n = len(key)
    arr = [[0 for i in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            arr[c][n-1-r] = key[r][c]
    return arr
    
def rotate_180(key):
    n = len(key)
    arr = [[0 for i in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            arr[n-1-r][n-1-c] = key[r][c]
    return arr

def rotate_270(key):
    n = len(key)
    arr = [[0 for i in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            arr[n-1-r][r] = key[r][c]
    return arr


def right(key , lock):
    n = len(key)
    for i in range(n):
        for j in range(n):
            if lock[i][j] ==1 and key[i][j] == 1:
                return False
    return True

def solution(key ,lock):
    answer = True
    
    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
key2= [[0,0,0],[0,0,1],[0,1,0]]
right(key2 ,lock)
