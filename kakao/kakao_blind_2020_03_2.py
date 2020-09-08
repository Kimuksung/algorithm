import numpy as np
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

def check( key ,lock):
    n = len(key)
    for i in range(n):
        for j in range(n):
            if key[i][j] == lock[i][j] :
                return False
    return True  

def rotate_90(key):
    n = len(key)
    arr = [[0 for i in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            arr[c][n-1-r] = key[r][c]
    return arr

def all_case(lock):
    n = len(lock)
    arr = [[0 for i in range(3*n)]for _ in range(3*n)]
    
    #initialize
    for i in range(n):
        for j in range(n):
            arr[i][j] = lock[i][j]
    
    useful_answer = []
    useful_answer.append(np.array(arr)[n:2*n,n:2*n])
    
    arr2 = arr
    for i in range(n*2):
        arr2 = moving(arr2 , "r")
        useful_answer.append(np.array(arr2)[n:2*n,n:2*n])
    
    for i in range(n*2):
        arr = moving(arr,"d")
        arr2 = arr
        for i in range(2*n):
            arr2 = moving(arr2 , "r")
            useful_answer.append(np.array(arr2)[n:2*n,n:2*n])
    
    return useful_answer

def solution(key, lock):
    answer = False
    
    useful_answer = all_case(lock)
    useful_key = []
    useful_key.append(key)
    print(useful_answer)
    for i in range(3):
        key = rotate_90(key)
        useful_key.append(key)
        
    for locks in useful_answer:
        for keys in useful_key:
            if check(keys ,locks) == True:
                return True
    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

solution(key, lock)

