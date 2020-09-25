histogram = [2, 2, 2, 3]
n = len(histogram)
max_num = 0

for i in range(n-1):
    for j in range(i+1,n):        
        temp = min(histogram[i] , histogram[j]) * (j-i-1)
        if temp > max_num:
            max_num = temp
            
print(max_num)
        
        
def solution(N):

    vertical = [1]
    horizon = [0]
    for i in range(N-1):
        x = vertical[-1] + horizon[-1]
        y = vertical[-1]
        vertical.append(x)
        horizon.append(y)
        print(vertical)
        print(horizon)
    answer = vertical[N-1] + horizon[N-1]

    return answer

solution(10)
