n = 10

def find_min(n , n_list):
    arr = []
    if n%2 ==0:
        arr.append(n_list[int(n/2)])
    if n%3 ==0:
        arr.append(n_list[int(n/3)])
    arr.append(n_list[n-1])
    return min(arr)

def solution(n):
    n_list = [0 for i in range(n+1)]
    
    for i in range(2,n+1):
        n_list[i] = find_min(i,n_list) +1
    
    return n_list
        
print(solution(n)[n])
