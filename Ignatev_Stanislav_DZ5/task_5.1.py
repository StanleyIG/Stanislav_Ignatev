def odd_nums(n):
    for i in range(n):
        i += 1
        yield i

odd_to_15 = odd_nums(15)
print(next(odd_to_15), next(odd_to_15), next(odd_to_15), next(odd_to_15), next(odd_to_15))
for i in odd_to_15:
    print(i)

#генератор запомнил какое псоледнее число было сгенерировано методом next() и с
# этого же числа вернул значения из цикла



