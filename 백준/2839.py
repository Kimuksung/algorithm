n = int(input())
list = [5001 for i in range(5000)]
list.insert(0,0)
list[3] = 1
list[5] = 1

if n>5:
    for i in range(6,n+1):
        list[i] = min(list[i-3] , list[i-5])+1

if list[n] > 5000:
    answer = -1
else:
    answer = list[n]

print(answer)