def solution(cardNumber):
    n = len(cardNumber)
    count = 0
    
    if n % 2 == 1: #홀수 경우
        for index , number in enumerate(cardNumber):  

            if index %2 == 1:
                temp = int(number) * 2
                if temp >= 10:
                    count += 1
                    count += (temp % 10)
                else:
                    count += temp
            else:
                count+= int(number)
        if count%2==0 :
            return "VALID"
        else:
            return "INVALID"
    
    else: #짝수 경우
        for index , number in enumerate(cardNumber):  

            if index %2 == 0:
                temp = int(number) * 2
                if temp >= 10:
                    count += 1
                    count += (temp % 10)
                else:
                    count += temp
            else:
                count+= int(number)
        if count%2==0 :
            return "VALID"
        else:
            return "INVALID"
        

cardNumber = "00000"
solution(cardNumber)