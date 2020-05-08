def solution(board, moves):
    answer = 0
    arr = []
    
    for move in moves:
        for doll in board:
            if doll[move-1] != 0:
                arr.append(doll[move-1])
                doll[move-1]=0
                break
        arr_len=len(arr)
        if arr_len>=2:
            if arr[arr_len-1] == arr[arr_len-2]:
                arr.pop()
                arr.pop()
                answer = answer+2
    
    
    return answer