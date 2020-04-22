import sys

temp = [[0 for j in range(253)] for i in range(253)]
temp2 = [[True for j in range(253)] for i in range(253)]

n,m = map(int,input().split())

for i in range(n):
    a = sys.stdin.readline().strip()
    for j in range(m):
        data=0
        if a[j]==".":
            data=1
        elif a[j]=="#":
            data=0
        elif a[j]=="v":
            data=2
        elif a[j]=="o":
            data=3
        temp[i+1][j+1] = int(data)

def DFS(row,col):
    wolf = 0
    sheep = 0
    stack = [[row+1,col+1]] #stack에 자신을 쌓는다.
    temp2[row+1][col+1] = False
    while True:
        #print("stack :" , stack)
        #stack이 비어있다면 종료
        if len(stack) == 0:
            if wolf >=sheep:
                sheep=0
            else:
                wolf=0
            #print("sheep:",sheep,"wolf:",wolf)
            return wolf, sheep

        node = stack.pop() #맨 위의 node
        x= node[0]
        y= node[1]

        if temp[x][y] == 2 :
            wolf +=1
        elif temp[x][y] == 3 :
            sheep += 1

        #if temp[x][y] == 0:
            #return node

        #node expand 위 아래 오른쪽 왼쪽
        if temp[x+1][y] !=0 and temp2[x+1][y] == True:
            stack.append([x+1,y])
            temp2[x+1][y] =False
        if temp[x-1][y] !=0 and temp2[x-1][y] == True:
            stack.append([x-1,y])
            temp2[x - 1][y] = False
        if temp[x][y+1] !=0 and temp2[x][y+1] == True :
            stack.append([x,y+1])
            temp2[x][y+1] = False
        if temp[x][y-1] !=0 and temp2[x][y-1] == True:
            stack.append([x,y-1])
            temp2[x][y-1] = False

wolf = 0
sheep = 0

for i in range(n):
    for j in range(m):
        if temp[i+1][j+1] != 0 and temp2[i+1][j+1] ==True:

            wolf2 , sheep2 = DFS(i,j)
            wolf += wolf2
            sheep += sheep2

print(sheep, wolf )

