a , b ,c = map(int , input().split() )

high =0
if (c - b ) % (a - b) ==0:
    answer = (c - b ) // (a - b)
else:
    answer = (c - b ) // (a - b) +1

print(answer)
