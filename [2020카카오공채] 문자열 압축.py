#[2020카카오공채] 문자열 압축

def function1(x,y):
    seq=x
    length=y
    return [seq[i:i+length] for i in range(0, len(seq), length)]

def function2(seq):
    answer=""
    i=0

    n=len(seq)
    count = 0
    check = seq[0]
    
    while(i<n):
        for tp in seq:
            if check==tp:
                count = count +1
                #print("출력")
            else:
                break
        if count!=1:
            answer += str(count)+seq[0]    
        else:
            answer += seq[0] 
        for t in range(0,count):
            del seq[0]
        i=i+count

        if not seq:
            break
        check=seq[0]
        count=0
        
    return len(answer)
    
#temp="abababcdcd"#0부터 시작
#seq=function1(temp,2)
#print(function2(seq))
#temp2="ababababcd"

temp="ababcdcdababcdcd"
answer=[]
for i in range(1,len(temp)):
    answer.append(function2(function1(temp,i)))
print(min(answer))