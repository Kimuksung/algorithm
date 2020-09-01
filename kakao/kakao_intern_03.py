gems = 	["AA", "AB", "AC", "AA", "AC"]
answer =[]

bosuk = len(set(gems))
gems_len = len(gems)
l = 1
r = 1

while(l<= gems_len and r <= gems_len and r>=l):
    temp = len(set(gems[l-1:r]))
    if temp == bosuk:
        answer=[l,r]
        l+=1
    if temp < bosuk:
        r+=1
        
print(answer)