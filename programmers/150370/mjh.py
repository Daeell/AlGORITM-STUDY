def solution(today, terms, privacies):
    answer = []

    Y, M, D = map(int, today.split('.'))

    term_types = {}
    for term in terms:
        term_type, period = term.split(' ')
        term_types[term_type] = int(period)

    for i in range(len(privacies)):
        date, term_type = privacies[i].split(' ')
        y, m, d = map(int, date.split('.'))
        month_period = term_types[term_type]
        if month_period >= 12:
            y += month_period//12
            month_period = month_period%12
        if m + month_period > 12:
            y += 1
            m = m + month_period - 12
        else:
            m += month_period
        if y < Y:
            answer.append(i+1)
            continue
        elif y == Y:
            if m < M:
                answer.append(i+1)
                continue
            elif m == M:
                if d <= D:
                    answer.append(i+1)
                    continue

    return answer

print(solution("2020.01.02", ["A 1"], ["2019.12.01 A"]))