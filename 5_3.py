def tutor_in_klass():
    tutors = [
        'Иван', 'Анастасия', 'Петр', 'Сергей',
        'Дмитрий', 'Борис', 'Елена'
    ]
    klasses = [
        # '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
        '9В', '8Б', '10А', '10Б', '9А']

    for _i in range(0, len(tutors)):
        tutor = tutors[_i]
        klass = klasses[_i] if _i < len(klasses) else None
        yield tutor, klass


print(tutor_in_klass())
print(*tutor_in_klass())
