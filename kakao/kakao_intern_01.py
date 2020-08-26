number = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

result = ""

current_left = "*"
current_right =  "#"

distance_dict = { 0 : [3,1] , 1 :[0,0] , 2:[0,1] , 3: [0,2] , 4:[1,0] , 5:[1,1] , 6:[1,2] , 7 :[2,0] , 8:[2,1] , 9:[2,2] , "*" :[3,0] , "#" :[3,2]}

def distance( a , b):
    a_x , a_y = distance_dict[a]
    b_x , b_y = distance_dict[b]
    answer = abs(b_x - a_x) + abs(b_y - a_y)
    
    return answer

for i in number:
    if i == 1 or i == 4 or i ==7 :
        current_left = i
        result += "L"
    elif i == 3 or i == 6 or i ==9 :
        current_right = i
        result += "R"
    
    else:
        left_distance = distance(current_left , i)
        right_distance = distance(current_right , i)
        if(left_distance < right_distance):
            result += "L"
            current_left = i
        elif(right_distance < left_distance):
            result += "R"
            current_right = i
        else:
            if hand == "left":
                result += "L"
                current_left = i
            else:
                result += "R"
                current_right = i
        
print(result)


    
        