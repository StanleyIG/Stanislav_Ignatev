tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Александр']
klasses = ['9А', '7В', '9Б']


# for i in range(len(tutors)):
# if i < len(tutors) and i < len(klasses):
# print((tutors[i], klasses[i]))
# else:
# if len(klasses) < len(tutors):
# print((tutors[i], None))
def tutor_class():
    for i in range(len(tutors)):
        if i < len(tutors) and i < len(klasses):
            yield tutors[i], klasses[i]
        elif len(klasses) < len(tutors):
            yield tutors[i], None


b = tutor_class()
print(type(b))
print(next(b), next(b), next(b), next(b))
for i in b:
    print(i)
