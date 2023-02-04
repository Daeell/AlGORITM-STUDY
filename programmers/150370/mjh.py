def solution(today, terms, privacies):
    answer = []

    Y, M, D = map(int, today.split('.'))

    term_types = {}
    for term in terms:
        term_type, period = term.split(' ')
        term_types[term_type] = period

    for i in range(len(privacies)):
        date, term_type = privacies[i].split(' ')
        y, m, d = map(int, date.split('.'))
        month_period = int(term_types[term_type])
        year_period = 0
        if month_period >= 12:
            year_period = month_period//12
            month_period = month_period%12
        if m + month_period > 12:
            year_period += 1
            month_period = m + month_period - 12
        if y + year_period < Y:
            answer.append(i+1)
            continue
        elif y + year_period == Y:
            if m + month_period < M:
                answer.append(i+1)
                continue
            elif m + month_period == M:
                if d-1 < D:
                    answer.append(i+1)
                    continue

    return answer

print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))