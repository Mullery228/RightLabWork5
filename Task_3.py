import sys
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Vadick', 'Chocoladick', 'Oleg']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def check_gen(tutors: list, klasses: list):
    for i in range(len(tutors)):
        kor = list()
        if len(klasses) - 1 - i >= 0:
            kor.append(tutors[i])
            kor.append(klasses[i])
        else:
            kor.append(tutors[i])
            kor.append(None)
        kor = tuple(kor)
        yield kor


generator = check_gen(tutors, klasses)
# добавьте здесь доказательство, что создали именно генератор
# потому что функция, где юзается иелд(yield) автоматически становится генератором(вроде бы да)
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
