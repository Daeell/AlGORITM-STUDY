def solution(record):
    answer = []
    
    _dict = {enter.split(" ")[1] : enter.split(" ")[2] for enter in record if enter.split(" ")[0] != "Leave"}
    
    for mes in record :
        if mes.split(" ")[0] == "Enter" :
            answer.append(_dict[mes.split(" ")[1]] + "님이 들어왔습니다.")
        elif mes.split(" ")[0] == "Leave" :
            answer.append(_dict[mes.split(" ")[1]] + "님이 나갔습니다.")

    
    return answer
