def solution(records):
    answers = []
    
    user_dict = dict()
    for record in records:
        command , user = record.split(" ", 1)
        if command =="Enter":
            user_id , nickname = user.split()
            user_dict[user_id] = nickname
            str = f"{user_id}님이 들어왔습니다."
            answers.append(str)
        elif command == "Leave":
            user_id = user
            str = f"{user_id}님이 나갔습니다."
            answers.append(str)
        elif command == "Change":
            user_id , nickname = user.split()
            user_dict[user_id] = nickname
    answer =[]
    for temp in answers:
        user_id , string =temp.split("님")
        answer.append(user_dict[user_id]+"님"+string)
    return answer

records = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(records)

