input1 = input().upper()

if len(input1) >1:
    alphadict = dict()
    for i in input1:
        if i in alphadict:
            alphadict[i] += 1
        else:
            alphadict[i] = 1
    
    sort_alpha = sorted(alphadict.items() , key = lambda x:x[1] , reverse = True)
    if sort_alpha[0][1] != sort_alpha[1][1]:
        print(sort_alpha[0][0])
    else:
        print("?")    
else:
    print(input1)