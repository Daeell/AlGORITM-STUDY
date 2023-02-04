def convertDate(date):
    year, month, day = map(int, date.split('.'))
    return (year * 12 * 28) + (month * 28) + day


def solution(today, terms, privacies):
    answer = []
    today_days = convertDate(today)
    
    terms_info = dict()
    for term in terms:
        a,b = term.split()
        terms_info[a] = int(b) * 28
  
    for i in range(len(privacies)):
        day, grade = privacies[i].split()
        if convertDate(day)-1+terms_info[grade] < today_days:
            answer.append(i+1)
    
        
    return answer
