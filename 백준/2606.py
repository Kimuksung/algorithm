import sys
n = sys.stdin.readline()
m = sys.stdin.readline()

n = int(n)
m = int(m)

temp = [i for i in range(n+1)]

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
    x,y = sys.stdin.readline().split()
    x = int(x)
    y = int(y)
    Union(x,y)

cnt = 0
for i in range(2,n+1):
    if Find(1) == Find(temp[i]):
        cnt+=1

print(cnt)