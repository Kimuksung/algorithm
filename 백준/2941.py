alphaset = ["c=" , "c-" , "dz=" , "d-" , "lj" , "nj" , "s=" , "z="]

input1 = input()

count = 0
for change in alphaset:
    count += input1.count(change)
    
answer = len(input1) - count
print(answer)