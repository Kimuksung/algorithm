import numpy as np

def rotate_90(key):
    n = len(key)
    arr = [[0 for i in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            arr[c][n-1-r] = key[r][c]
    return arr

def new_map(key):
    n = len(key) 
    temp_map = [[1 for i in range(3*n)] for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            temp_map[i][j] = key[i][j]
    return temp_map

def moving( arr , direct ):
    n = len(arr)
    
    temp_arr = [[0 for i in range(n)] for _ in range(n)]
    
    if direct == "r":
        for i in range(n-1):
            for j in range(n-1):
                temp_arr[i][j+1] = arr[i][j]
    if direct == "d":
        for i in range(n-1):
            temp_arr[i+1] =  arr[i]
    
    return temp_arr

def middle(arr):
    n = len(arr) //3
    return np.array(arr)[n:2*n, n:2*n]

def check( arr , lock ):
    n = len(lock)
    arr = middle(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] == lock[i][j]:
                return False
    return True

def solution(key, lock):
    answer = False
    n = len(key)
    
    for i in range(4):
        key = rotate_90(key)
        temp_map = new_map(key)
        
        if check(temp_map , lock): # 가운데 추출했을 때 똑같다면
            return True
        
        for j in range(n*2):
            temp_map = moving(temp_map,"d")
            if check(temp_map , lock):
                return True
            temp_map2 = temp_map
            
            for t in range(n*2):
                temp_map2 = moving(temp_map2,"r")
                if check(temp_map2 , lock):
                    return True
        
    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]	
solution(key,lock)
