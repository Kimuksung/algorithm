import sys
n , m  = sys.stdin.readline().split()
n = int(n)
m = int(m)
temp = [ i  for i in range(1000001)]

def Find(x):
    if temp[x] == x:
        return x
    else:
        p = Find(temp[x])
        temp[x] = p
        return p

def Union(x,y):
    x=Find(x)
    y=Find(y)

    if(x!=y):
        temp[y]=x


for i in range(m):
    data = sys.stdin.readline().split()
    data[0]= int(data[0])
    data[1]= int(data[1])
    data[2]= int(data[2])

    if data[0]==0:
        Union(data[1],data[2])
    else:
        if Find(data[1])==Find(data[2]):
            print("YES")
        else:
            print("NO")
