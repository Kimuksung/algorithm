from math import gcd

def solution(w,h):
    answer = w*h
    multiple = gcd(w,h)
    
    if multiple != 1:
        w = w/multiple
        h = h/multiple
    
    no_rectangle = w + h - 1
    answer -= no_rectangle * multiple
    
    return answer