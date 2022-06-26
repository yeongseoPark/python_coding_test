def solution(record):
    answer = []
    dic = {}
    for i in record:
        space_index =  [k for k,v in enumerate(i) if v == " "]
        if i[0] == "E":
            dic[i[space_index[0]+1:space_index[1]]] = i[space_index[1]+1:] # uid1234 : muzi  형식으로 저장 
            answer.append("{}님이 들어왔습니다.".format(i[space_index[0]+1:space_index[1]]))  # uid1234님이 들어왔습니다.(임시)

        elif i[0] == "C":
            dic[i[space_index[0]+1:space_index[1]]] = i[space_index[1]+1:] # uid1234 : prodo 형식

        elif i[0] == "L":
            answer.append("{}님이 나갔습니다.".format(i[space_index[0]+1:])) # uid1234님이 나갔습니다. 형식
    
    real_answer = []
    for i in answer: # uid1234 를 이름으로 바꿔줌
        index = i.find("님")
        new = dic[i[:index]]
        i = new + i[index:]
        real_answer.append(i)
        

    return real_answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))