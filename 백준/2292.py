input1 = int(input())

answer = 1
number= 1

if input1 != 1:
    for i in range(1,1000000000):
        number += 6*i
        if number >= input1:
            answer = i + 1
            break
else:
    answer = 1
    
print(answer)