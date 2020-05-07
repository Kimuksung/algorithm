# -*- coding: utf-8 -*-
import sys 
sys.setrecursionlimit(10**8)

t = int(input())

for i in range(t):

    arr1 = [0]*100000
    arr2 = [0]*100000
    
    dp1 = [0]
    dp2 = [0]
    n = int(input())    

    temp1 = list(map(int,input().split()))
    #temp1 = input().split()
    
    for i in range(n):
        arr1[i] = int(temp1[i])
    temp2 = input().split()
    for i in range(n):
        arr2[i] = int(temp2[i])
        
        
    if n==1:
        print(max(arr1[0] , arr2[0]))
        
    else:
        dp1.append(arr1[0])
        dp2.append(arr2[0])
       
        for i in range(2,n+1):

            dp1.append(max(arr1[i-1]+dp2[i-1],dp1[i-1],arr1[i-1]+dp2[i-2]) )
            dp2.append(max(arr2[i-1]+dp1[i-1],dp2[i-1],arr2[i-1]+dp1[i-2]))    

        answer = max(dp1[n],dp2[n])
    
        print(answer)
