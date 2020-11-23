n = int(input())
temp = []

for i in range(n):
    x , y = map(int , input().split())
    temp.append([x,y])

def solution(examples):
    answer = 0
    
    example = sorted(examples , key = lambda x:x[0] ) #순서대로 정렬
    
    max_number = max(y for x,y in example) # 제일 큰값 찾기
  
    x = example[0][0]
    y = example[0][1]
    min_index = 0 # 큰 값 x좌표 구하기 위한 값
    max_index = 0

    for i,j in example[1:]: #왼쪽부터 제일 높은 데까지
        if j >= max_number:
            answer += (i-x) * y
            min_index = i
            break
        
        if y < j :
            answer += (i-x) * y
            x = i
            y = j
    
    example = example[::-1]
    x = example[0][0]
    y = example[0][1]
    
    for i,j in example[1:]: #우측부터 제일 높은 데까지
        if j >= max_number:
            answer += (x-i) * y
            max_index = i
            break
        if y < j :
            answer += (x-i) * y
            x = i
            y = j
            
    answer += (max_index - min_index + 1) * max_number
    return answer
        
print(solution(temp))