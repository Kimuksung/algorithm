a , b , c = map(int , input().split())

if c-b>0:
    answer = int(a / (c-b)) + 1

else:
    answer = -1
print(answer)