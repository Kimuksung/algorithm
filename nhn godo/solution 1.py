def solution( goods):
    goods = sorted(goods , reverse = True)
    count = 0 
    keep = 0
    for good in goods:
        if good >= 50 :
            count += 1
        else:
            keep += good
        
        if keep >= 50:
            count += 1
            keep = 0
            
    return sum(goods) - 10* count
        
goods = [5,3,15]
solution(goods)