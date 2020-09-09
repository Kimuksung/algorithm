import numpy as np
import itertools

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

def out_of_one( arr , count):
    n = len(arr) // 3
    temp = []
    for i in range(n,3*n-1):
        for j in range(n,3*n-1):
            temp.append(arr[i][j])
    
    if temp.count(0) == count:
        return True
    return False

def all_case(lock , count):
    n = len(lock)
    all_n = 3*n
    arr = [[1 for i in range( all_n)] for _ in range( all_n ) ]
    answer = []
    for i in range(n):
        for j in range(n):
            arr[i][j] = lock[i][j]    
    
    if out_of_one(arr,count):
        answer.append( np.array(arr)[n:2*n, n:2*n])    
    
    for i in range(2*n):
        arr = moving(arr, "d")
        if out_of_one(arr,count):
            answer.append(np.array(arr)[n:2*n, n:2*n])
        arr2 = arr
        for j in range(2*n):
            arr2 = moving(arr2,"r")
            if out_of_one(arr2,count):
                answer.append(np.array(arr2)[n:2*n, n:2*n])
            
    return answer
                
def rotate_90(key):
    n = len(key)
    arr = [[0 for i in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            arr[c][n-1-r] = key[r][c]
    return arr

def all_case_key(key):
    arr = key
    answer =[]
    answer.append(arr)
    for i in range(3):
        arr = rotate_90(arr)
        answer.append(arr)
     
    return answer

def check(lock, key):
    n = len(key)
    for i in range(n):
        for j in range(n):
            if lock[i][j]== 0 and key[i][j]==0:
                return False
            if lock[i][j]== 1 and key[i][j]==1:
                return False
    return True

def solution(key, lock):
    answer = False
    count = list(itertools.chain.from_iterable(lock)).count(0)
    useful_lock = all_case(lock , count)
    useful_key = all_case_key(key)
    
    for use_lock in useful_lock:
        for use_key in useful_key:
            if check(use_lock , use_key):
                return True
    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
solution(key , lock)


key=[[0,0,0],[0,0,1],[0,1,0]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
check(lock,key)
