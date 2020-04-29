# DP

n = int(input())

wine_list = [int(input()) for i in range(n)]

dp = [0]

dp.append(wine_list[0])

if n>1 :
    dp.append(wine_list[0]+wine_list[1])
    
# 3가지
# 1) 내가 먹은날 3일이라면, 2일도 먹었음 그러면 1일 건너 뛰고 0일날 꺼
# 2) 내가 먹은날 3일이라면, 2일 안먹었음 그러면 1일날거 추가
# 3) 내가 안먹으면 전날꺼
# 위 3개 큰 값
    
for i in range(3,n+1):    
    first_case = wine_list[i - 1 ] + wine_list[i -2 ] + dp[i-3]
    second_case = wine_list[i-1] +dp[i-2]
    third_case = dp[i-1]
    
    dp.append(max(first_case , second_case , third_case))

print(dp[n])
