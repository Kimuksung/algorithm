s = "aaaaabbbbccc"    
n = 2

str_dict = dict()

for char in s:
    if char in str_dict.keys():
        str_dict[char] += 1
    else:
        str_dict[char] = 1

test = list(str_dict.values())
test = sorted(test)

temp = []
if n>=sum(test[:-1]):
    temp.append(0)
else:
    test2 = test.copy()

    for i in range(n):
        test[-1] -= 1
        test = sorted(test)
        test = [i for i in test if i != 0]

        temp.append( test[-1] - test[0] )
    
    if test2[0] <= n:
        n = n - test2[0]
        test2 = test2[1:]

    for i in range(n):
        test2[0] -= 1
        test2 = sorted(test2)
        test2 = [i for i in test2 if i != 0]

        temp.append( test2[-1] - test2[0] )
        

print( min(temp) )

'''
문제 설명
문자열 s의 거친 정도는 다음과 같이 계산할 수 있다. s에서 가장 많이 등장하는 글자를 c1이라 하고, 가장 적게 등장하는 글자를 c2라 한다 (c2는 반드시 한번 이상은 등장해야 한다). s의 거친 정도는 c1이 등장하는 횟수에서 c2가 등장하는 횟수를 뺀 숫자이다.

당신은 주어진 문자열 s에서 0개 이상, n개 이하의 글자를 삭제하는 방법으로 문자열을 변경할 수 있다 (명확한 이해를 위해 예제를 참조하라). 이 방법을 이용하여 얻을 수 있는 가장 적은 문자의 거친 정도를 반환하여라.

참고 / 제약 사항
s는 1개 이상, 50개 이하의 글자를 가진다.
s는 소문자만 가진다 ('a'-'z').
n은 0이상, m-1이하이다. 이 때, m은 s에 있는 글자의 개수이다.

테스트 케이스
s = "aaaaabbc"
n = 1리턴(정답): 3
하나의 'a'를 삭제하거나 하나의 'c'를 삭제하여 최소의 거친 정도 3을 얻을 수 있다.

s = "aaaabbbbc"
n = 5리턴(정답): 0
'c'와 모든 'a'를 지우는 방법이 있다.
'''