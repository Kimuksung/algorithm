import re
expression = "50*6-3*2"
number = re.split( '[-*+]', expression)
operator = []
for i in expression:
    if i =="-" or i=="+" or i=="*":
        operator.append(i)
        
print(number)
print(operator)

result = []

from itertools import permutations
permute = list(permutations(["*" , "+" ,"-"] , 3))

for i in permute:
    temp = list(i)

#temp = list(permute[0])

    number2 = []
    number2.append( int(number.pop(0)))
    oper2 = []
    for oper in temp:  
        for index in operator:
            print("oper:" , index)
            print("num data : " ,number)
            print("num data2 : " ,number2)
            pop_num = int(number.pop(0))
            pop_num2 = number2.pop()
        
            if index == oper:
                if oper == "*":
                    number2.append( pop_num2 * pop_num)
                elif oper == "-":
                    number2.append( pop_num2 - pop_num)
                else:
                    number2.append( pop_num2 + pop_num)
            else:
                number2.append(pop_num2)
                number2.append(pop_num)
                oper2.append(index)
        number = number2
        operator = oper2
        number2 = []
        number2.append( int(number.pop(0)))
        oper2 = []
    
    result.append(number2)
