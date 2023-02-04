from datetime import datetime, timedelta


def solution(today, terms, privacies):
    today_date = datetime.strptime(today, "%Y.%m.%d").date()
    answer = []

    for i in range(len(terms)):
        term = terms[i].split()
        term_duration = int(term[1])
        start_date = today_date - timedelta(days=term_duration)

        privacy_date = datetime.strptime(
            privacies[i].split()[0], "%Y.%m.%d").date()
        if privacy_date <= start_date:
            answer.append(i + 1)

    return answer


def solution(today, terms, privacies):
    today_date = datetime.strptime(today, "%Y.%m.%d").date()
    answer = []

    for i in range(len(terms)):
        term = terms[i].split()
        term_letter = term[0]
        term_duration = int(term[1])
        start_date = today_date - timedelta(days=term_duration)

        for privacy in privacies:
            privacy_split = privacy.split()
            privacy_letter = privacy_split[1]
            privacy_date = datetime.strptime(
                privacy_split[0], "%Y.%m.%d").date()

            if privacy_letter == term_letter and privacy_date >= start_date:
                answer.append(i + 1)
                break

    return answer


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], [
    "2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
# [1, 3]
print(solution("2020.01.01", ["Z 3", "D 5"], [
    "2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
# [1, 4, 5]
