import math

n = int(input())

arr = list(map(int , input().split()))
answer = []
b , c = map(int,input().split())

for i in arr:
    if i-b >0:
        i = i - b
    else:
        i=0
    answer.append(math.ceil(i/c))

ans = sum(answer) + n

print(ans)